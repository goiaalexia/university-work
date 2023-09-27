package Model.State;


import Model.DataStructures.*;
import Model.Exceptions.EvaluationException;
import Model.Exceptions.ExecutionException;
import Model.Exceptions.StackException;
import Model.Statements.IStatement;
import Model.Values.IValue;
import Model.Values.StringValue;

import java.io.BufferedReader;
import java.util.Collections;
import java.util.Random;
import java.util.TreeSet;


public class PrgState {
    public IStack<IStatement> exeStack;
    public IDictionary<String, IValue> symTable;
    public IList<String> out;

    public IDictionary<StringValue, BufferedReader> fileTable;
    public IHeap heap;
    public ILockTable lockTable;

    private static final TreeSet<Integer> ids = new TreeSet<>();
    public int id;

    public PrgState(IStatement originalProgram) {
        this.exeStack = new ADTStack<>();
        this.symTable = new ADTDictionary<>();
        this.out = new ADTList<>();
        this.fileTable = new ADTDictionary<>();
        this.heap = new ADTHeap();
        this.lockTable = new ADTLockTable();
        exeStack.push(originalProgram);
        this.id = newId();
    }

    // ADDED FOR MULTITHREADING AND MANAGING THE IDs OF THE STATE
    private static Integer newId() {
        Random random = new Random();
        Integer id;
        synchronized (ids) {
            do {
                id = random.nextInt();
            } while (ids.contains(id));
            ids.add(id);
        }
        return id;
    }

    public int getId() {
        return id;
    }

    public PrgState(IStack<IStatement> executionStack, IDictionary<String, IValue> symTable, IList<String> out, IDictionary<StringValue, BufferedReader> fileTable, IHeap heap, ILockTable lockTable) {
        this.exeStack = executionStack;
        this.symTable = symTable;
        this.out = out;
        this.fileTable = fileTable;
        this.heap = heap;
        this.lockTable = lockTable;
    }

    public ILockTable getLockTable() {
        return lockTable;
    }

    public IStack<IStatement> getExeStack() {
        return exeStack;
    }

    public IDictionary<String, IValue> getSymTable() {
        return symTable;
    }

    public IList<String> getOut() {
        return out;
    }

    public IDictionary<StringValue, BufferedReader> getFileTable() {
        return fileTable;
    }

    public IHeap getHeap() {
        return heap;
    }

    public boolean isNotCompleted() {
        return !exeStack.isEmpty();
    }

    // ADDED FOR MULTITHREADING
    public PrgState oneStep() throws EvaluationException, ExecutionException, StackException {
        if (exeStack.isEmpty())
            throw new ExecutionException("Exe stack is empty!");
        IStatement currentStatement = exeStack.pop(); // get first statement
        return currentStatement.execute(this); // execute the statement
    }

    public String executionStackToString() {
        StringBuilder executionStackStringBuilder = new StringBuilder();

        for (IStatement statement : exeStack) {
            executionStackStringBuilder.append(statement.toString()).append("|");
        }

        return executionStackStringBuilder.toString();
    }

    public String symTableToString() {
        StringBuilder symbolTableStringBuilder = new StringBuilder();

        for (String key : Collections.list(symTable.keys())) { // enumeration to list
            symbolTableStringBuilder.append(String.format("%s -> %s\n", key, symTable.get(key).toString()));
        }

        return symbolTableStringBuilder.toString();
    }

    public String outToString() {
        StringBuilder outStringBuilder = new StringBuilder();

        for (String object : out) {
            outStringBuilder.append(object).append("\n");
        }

        return outStringBuilder.toString();
    }

    public String fileTableToString() {
        StringBuilder fileTableStringBuilder = new StringBuilder();

        for (StringValue key : Collections.list(fileTable.keys())) { // enumeration to list
            fileTableStringBuilder.append(String.format("%s -> %s\n", key.toString(), fileTable.get(key).toString()));
        }

        return fileTableStringBuilder.toString();
    }

    public String heapToString() {
        StringBuilder heapStringBuilder = new StringBuilder();

        for (Integer position : heap.getContent().keySet()) {
            heapStringBuilder.append(position).append(" -> ").append(heap.getContent().get(position).toString()).append("\n");
        }

        return heapStringBuilder.toString();

    }

    public String lockTableToString() throws EvaluationException {
        StringBuilder lockTableStringBuilder = new StringBuilder();
        for (int key : lockTable.keySet()) {
            lockTableStringBuilder.append(String.format("%d -> %d\n", key, lockTable.get(key)));
        }
        return lockTableStringBuilder.toString();
    }

    @Override
    public String toString() {
        return String.format("ID: %d\n\n~ EXECUTION STACK ~\n%s\n~ SYMBOL TABLE ~\n%s\n~ OUTPUT ~\n%s\n~ FILE TABLE ~\n%s\n~ HEAP ~\n%s\n~ LOCK TABLE ~\n%s\n", id, executionStackToString(), symTableToString(), outToString(), fileTableToString(), heapToString(), lockTable.toString());
    }

    public String programStateToString() throws EvaluationException {
        return "Id: " + id + "\nExecution stack: \n" + executionStackToString() + "Symbol table: \n" + symTableToString() + "Output list: \n" + outToString() + "File table:\n" + fileTableToString() + "Heap memory:\n" + heapToString() + "Lock Table:\n" + lockTableToString();
    }

    @Deprecated
    public PrgState oneStepSingleThreaded() throws StackException, ExecutionException, EvaluationException {

        IStatement top = exeStack.pop();
        return top.execute(this);

    }
}