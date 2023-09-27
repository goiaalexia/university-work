package Controller;

import Model.DataStructures.ADTDictionary;
import Model.DataStructures.ADTStack;
import Model.DataStructures.IDictionary;
import Model.DataStructures.IStack;
import Model.Exceptions.*;
import Model.State.PrgState;
import Model.Statements.IStatement;
import Model.Types.IType;
import Model.Types.RefType;
import Model.Values.IValue;
import Model.Values.RefValue;
import Repository.*;

import java.io.IOException;
import java.util.*;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;

public class Controller {

    private final IRepository repository;

    public ExecutorService executor;

    public String logFilePath;

    public boolean stepByStep;


    public Controller() {
        repository = new Repository("C:\\Users\\lexig\\IdeaProjects\\a3\\logFile");
        this.stepByStep = false;
    }

    public Controller(String s, boolean stepByStep) {
        logFilePath = s;
        repository = new Repository(logFilePath);
        this.stepByStep = stepByStep;
    }

    public Controller(String s, boolean stepByStep, IStatement c) {
        logFilePath = s;
        repository = new Repository(logFilePath);
        this.stepByStep = stepByStep;
        this.addProgram(c);
    }

    public Controller(IRepository r) {
        logFilePath = r.getLogFilePath();
        repository = r;
        this.stepByStep = false;
    }

    public IRepository getRepository() {
        return repository;
    }

    public void addProgram(IStatement statement) {
        repository.addProgramState(new PrgState(statement));
    }

    Map<Integer, IValue> safeGarbageCollector(IDictionary<String, IValue> symbols, Map<Integer, IValue> heap) {
        HashMap<Integer, IValue> newHeap = new HashMap<>();

        for (IValue val : Collections.list(symbols.elements())) {
            if (val instanceof RefValue) {
                int address = ((RefValue) val).getAddr();
                if (heap.containsKey(address)) {
                    newHeap.put(address, heap.get(address));
                }

                if (val.getType() instanceof RefType) {
                    if (heap.containsKey(address)) {
                        IValue value = heap.get(address);
                        while (value instanceof RefValue) {
                            int address2 = ((RefValue) value).getAddr();
                            if (heap.containsKey(address2)) {
                                newHeap.put(address2, heap.get(address2));
                            }
                            value = heap.get(address2);
                        }
                    }
                }
            }
        }
        return newHeap;
    }


    Map<Integer, IValue> garbageCollector(Set<Integer> symTableAddr, Map<Integer, IValue> heap) {
        return heap.entrySet().stream()
                .filter(e -> symTableAddr.contains(e.getKey()))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    public void oneStepForEachProgram(List<PrgState> programStateList) throws EvaluationException, ExecutionException {
        programStateList.forEach(prg -> {
            try {
                repository.logProgramStateExecution(prg);
            } catch (IOException e) {
                System.out.println(e.getMessage());
                System.exit(1);
            }
        }); // log file for every state
        // list of callables
        List<Callable<PrgState>> callList = programStateList.stream()
                .map((PrgState p) -> (Callable<PrgState>) (p::oneStep))
                .collect(Collectors.toList());


        List<PrgState> newProgramsList = null;
        try {
            newProgramsList = executor.invokeAll(callList).stream()
                    .map(future ->
                    {
                        try {
                            return future.get();
                        } catch (java.util.concurrent.ExecutionException | InterruptedException ex) {
                            System.out.println(ex.toString());
                        }
                        return null;
                    })
                    .filter(Objects::nonNull).toList();

        } catch (InterruptedException e) {
            System.out.println(e.getMessage());
        }

        programStateList.addAll(newProgramsList);
        programStateList.forEach(prg -> {
            prg.getHeap().setContent(garbageCollector(getAddrFromSymTable(
                            programStateList.stream().map(programState -> programState.getSymTable().getContent().values()).collect(Collectors.toList()),
                            prg.getHeap().getContent()
                    ),
                    prg.getHeap().getContent()));
        });

        /// We save again all the program states, including the old and the new ones to a file
        // we have to use print, because we cannot handle the errors otherwise.
        programStateList.forEach(p -> {
            try {
                this.repository.logProgramStateExecution(p);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        });

        this.repository.setProgramStates(programStateList);
    }

    public void runTypeChecker() throws EvaluationException, StackException {
        for (PrgState state : repository.getProgramStates()) {
            IDictionary<String, IType> typeTable = new ADTDictionary<>();
            state.getExeStack().peek().typeCheck(typeTable);
        }
    }

    List<PrgState> removeCompletedPrograms(List<PrgState> programStateList) {
        return programStateList.stream()
                .filter(PrgState::isNotCompleted)
                .collect(Collectors.toList());
    }

    Set<Integer> getAddrFromSymTable(List<Collection<IValue>> symTableValues, Map<Integer, IValue> heap) {
        Set<Integer> toReturn = new TreeSet<>();
        symTableValues.forEach(symTable -> symTable.stream()
                .filter(v -> v instanceof RefValue)
                .forEach(v -> {
                    while (v instanceof RefValue) {
                        toReturn.add(((RefValue) v).getAddr());
                        v = heap.get(((RefValue) v).getAddr());
                    }
                }));

        return toReturn;
    }

    // DEPRECATED BECAUSE OF MULTITHREADING
    @Deprecated
    public void executeOneStep(PrgState programState) throws EvaluationException, ExecutionException, StackException {
        IStack<IStatement> executionStack = programState.getExeStack(); // get the stack

        IStatement currentStatement = executionStack.pop(); // get first statement
        currentStatement.execute(programState); // execute the statement

        displayCurrentState(programState); // display state after execution
    }

    // DEPRECATED BECAUSE OF MULTITHREADING
    @Deprecated
    public void executeAllSteps() throws EvaluationException, ExecutionException, StackException {
        PrgState currentProgramState = repository.getCurrentProgramState(); // get state

        displayCurrentState(currentProgramState); // display state
        try {
            repository.logProgramStateExecution(currentProgramState);
        } catch (IOException e) {
            System.out.println(e.getMessage());
            System.exit(1);
        }

        while (!currentProgramState.getExeStack().isEmpty()) { // while we can still execute commands
            executeOneStep(currentProgramState);

            currentProgramState.getHeap().setContent(safeGarbageCollector(currentProgramState.getSymTable(), currentProgramState.getHeap().getContent()));
            try {
                repository.logProgramStateExecution(currentProgramState);
            } catch (IOException e) {
                System.out.println(e.getMessage());
                System.exit(1);
            }

        }
    }

    // EDITED FOR MULTITHREADING, CLI
    public void stepByStepExecution() throws EvaluationException, ExecutionException, StackException {
        runTypeChecker();
        // this only needs to be run once, therefore it's redundant
        executor = Executors.newFixedThreadPool(16);
        List<PrgState> prgList = removeCompletedPrograms(repository.getProgramStates());

        // problematic if left unchecked
        Scanner inputBestie = new Scanner(System.in);

        int stepCount = 1;
        String inputForStep;

        while (prgList.size() > 0) {
            System.out.println("Step " + stepCount + ":");
            inputForStep = inputBestie.nextLine();
            stepCount++;
            oneStepForEachProgram(prgList);
            //remove the completed programs
            prgList = removeCompletedPrograms(repository.getProgramStates());
        }

        executor.shutdownNow();

        // HERE the repository still contains at least one Completed Prg
        // and its List<PrgState> is not empty. Note that oneStepForAllPrg calls the method
        // setPrgList of repository in order to change the repository
        //
        // update the repository state
        repository.setProgramStates(prgList);

    }


    public void takeAStepForGUI() throws EvaluationException, ExecutionException, StackException {
        executor = Executors.newFixedThreadPool(16);
        List<PrgState> prgList = removeCompletedPrograms(repository.getProgramStates());

        // problematic if left unchecked
//        Scanner inputBestie = new Scanner(System.in);

//        int stepCount = 1;
//        String inputForStep;

        if (prgList.size() > 0) {
//            System.out.println("Step " + stepCount + ":");
//            inputForStep = inputBestie.nextLine();
//            stepCount++;
            oneStepForEachProgram(prgList);
            //remove the completed programs
            prgList = removeCompletedPrograms(repository.getProgramStates());
        }

        executor.shutdownNow();

        // HERE the repository still contains at least one Completed Prg
        // and its List<PrgState> is not empty. Note that oneStepForAllPrg calls the method
        // setPrgList of repository in order to change the repository
        //
        // update the repository state
        repository.setProgramStates(prgList);

    }

    // ADDED FOR MULTITHREADING
    public void allStep() throws ExecutionException, EvaluationException, StackException {
        runTypeChecker();
        executor = Executors.newFixedThreadPool(16);
        //remove the completed programs
        List<PrgState> prgList = removeCompletedPrograms(repository.getProgramStates());
        while (prgList.size() > 0) {
            oneStepForEachProgram(prgList);
            //remove the completed programs
            prgList = removeCompletedPrograms(repository.getProgramStates());
        }

        executor.shutdownNow();

        // HERE the repository still contains at least one Completed Prg
        // and its List<PrgState> is not empty. Note that oneStepForAllPrg calls the method
        // setPrgList of repository in order to change the repository
        //
        // update the repository state
        repository.setProgramStates(prgList);
    }


    public void displayCurrentState(PrgState programState) {
        System.out.println(programState.toString() + "\n");
    }
}