package View.GUI;

import Controller.Controller;
import Model.DataStructures.*;
import Model.State.PrgState;
import Model.Statements.IStatement;
import Model.Values.IValue;
import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.scene.control.*;


import java.util.*;
import java.util.stream.Collectors;

class Pair<T1, T2> {
    T1 first;
    T2 second;

    public Pair(T1 first, T2 second) {
        this.first = first;
        this.second = second;
    }
}

public class ProgramRunController {
    private Controller controller;

    @FXML
    private TableView<Pair<Integer, IValue>> heapTable;



    @FXML
    private TableColumn<Pair<Integer, IValue>, Integer> addressColumn;

    @FXML
    private TableColumn<Pair<Integer, IValue>, String> valueColumn;

    @FXML
    private ListView<String> outputList;

    @FXML
    private ListView<String> fileList;

    @FXML
    private ListView<Integer> programStateList;

    @FXML
    private ListView<String> executionStackList;

    @FXML
    private TableView<Pair<String,IValue>> symbolTable;

    @FXML
    private TableView<Pair<Integer,Integer>> lockTableView;

    @FXML
    private TableColumn<Pair<Integer, Integer>, String> locationColumn;

    @FXML
    private TableColumn<Pair<Integer, Integer>, String> lockValueColumn;
    @FXML
    private TableColumn<Pair<String, IValue>, String> symVariableColumn;

    @FXML
    private TableColumn<Pair<String, IValue>, String> symValueColumn;

    @FXML
    private TextField numberOfProgramStates;

    @FXML
    private Button oneStep;

    @FXML
    public void initialize() {
        addressColumn.setCellValueFactory(p -> new SimpleIntegerProperty(p.getValue().first).asObject());
        valueColumn.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().second.toString()));
        symVariableColumn.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().first));
        symValueColumn.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().second.toString()));
        locationColumn.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().first.toString()));
        lockValueColumn.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().second.toString()));
        oneStep.setOnAction(actionEvent -> {
            if(controller == null){
                Alert alert = new Alert(Alert.AlertType.ERROR, "The program was not selected", ButtonType.OK);
                alert.showAndWait();
                return;
            }

            boolean programStateLeft = Objects.requireNonNull(getCurrentProgramState()).getExeStack().isEmpty();
            if(programStateLeft){
                Alert alert = new Alert(Alert.AlertType.ERROR, "Nothing left to execute", ButtonType.OK);
                alert.showAndWait();
                return;
            }

            try {
                controller.takeAStepForGUI(); // ?????????
                populate();
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
        });
        programStateList.setOnMouseClicked(mouseEvent -> populate());
    }

    private PrgState getCurrentProgramState(){
        if (controller.getRepository().getProgramStates().size() == 0)
            return null;
        int currentId = programStateList.getSelectionModel().getSelectedIndex();
        if (currentId == -1)
            return controller.getRepository().getProgramStates().get(0);
        return controller.getRepository().getProgramStates().get(currentId);
    }

    public void setController(Controller controller) {
        this.controller = controller;
        populate();
    }

    private void populate() {
        populateHeap();
        populateProgramStateIdentifiers();
        populateFileTable();
        populateOutput();
        populateSymbolTable();
        populateExecutionStack();
        populateLockTableView();
    }

    private void populateLockTableView() {
        PrgState programState = getCurrentProgramState();
        ILockTable lockTable = Objects.requireNonNull(programState).getLockTable();
        ArrayList<Pair<Integer, Integer>> lockTableEntries = new ArrayList<>();
        for(Map.Entry<Integer, Integer> entry: lockTable.getContent().entrySet()) {
            lockTableEntries.add(new Pair<>(entry.getKey(), entry.getValue()));
        }
        lockTableView.setItems(FXCollections.observableArrayList(lockTableEntries));
    }

    private void populateHeap() {
        IHeap heap;
        if (controller.getRepository().getProgramStates().size() > 0)
            heap = controller.getRepository().getProgramStates().get(0).getHeap();
        else heap = new ADTHeap();
        List<Pair<Integer, IValue>> heapTableList = new ArrayList<>();
        for (Map.Entry<Integer, IValue> entry : heap.getContent().entrySet())
            heapTableList.add(new Pair<>(entry.getKey(), entry.getValue()));
        heapTable.setItems(FXCollections.observableList(heapTableList));
        heapTable.refresh();
    }

    private void populateProgramStateIdentifiers() {
        List<PrgState> programStates = controller.getRepository().getProgramStates();
        var idList = programStates.stream().map(PrgState::getId).collect(Collectors.toList());
        programStateList.setItems(FXCollections.observableList(idList));
        numberOfProgramStates.setText("" + programStates.size());
    }

    private void populateFileTable() {
        ArrayList<String> files;
        if (controller.getRepository().getProgramStates().size() > 0)
            files = Collections.list(controller.getRepository().getProgramStates().get(0).getFileTable().keys()).stream().map(Object::toString).collect(Collectors.toCollection(ArrayList::new));
        else files = new ArrayList<>();
        fileList.setItems(FXCollections.observableArrayList(files));
    }

    private void populateOutput() {
        IList<String> output;
        if (controller.getRepository().getProgramStates().size() > 0)
            output = controller.getRepository().getProgramStates().get(0).getOut();
        else output = new ADTList<>();
        outputList.setItems(FXCollections.observableList(output.getList()));
        outputList.refresh();
    }

    private void populateSymbolTable() {
        PrgState state = getCurrentProgramState();
        List<Pair<String, IValue>> symbolTableList = new ArrayList<>();
        if (state != null)
            for (Map.Entry<String, IValue> entry : state.getSymTable().getContent().entrySet())
                symbolTableList.add(new Pair<>(entry.getKey(), entry.getValue()));
        symbolTable.setItems(FXCollections.observableList(symbolTableList));
        symbolTable.refresh();
    }

    private void populateExecutionStack() {
        PrgState state = getCurrentProgramState();
        List<String> executionStackListAsString = new ArrayList<>();
        if (state != null)
            for(IStatement s : state.getExeStack().getStack()){
                executionStackListAsString.add(s.toString());
            }
        executionStackList.setItems(FXCollections.observableList(executionStackListAsString));
        executionStackList.refresh();
    }
}