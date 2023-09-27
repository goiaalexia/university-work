package View.GUI;

import Controller.Controller;
import Model.Expressions.*;
import Model.State.PrgState;
import Model.Statements.*;
import Model.Types.BoolType;
import Model.Types.IntType;
import Model.Types.RefType;
import Model.Types.StringType;
import Model.Values.BoolValue;
import Model.Values.IntValue;
import Model.Values.StringValue;
import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;
import Repository.*;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class ProgramListSelector {
    private ProgramRunController programController;
    @FXML
    private List<IStatement> programStatements;

    public void setProgramController(ProgramRunController programController) {
        this.programController = programController;
    }

    @FXML
    private ListView<IStatement> programList;
    @FXML
    private Button displayButton;

    private void buildProgramList() {
        IStatement s1 = new CompoundStatement(new VarDeclarationStatement("v", new IntType()),
                new CompoundStatement(new AssignStatement("v", new ValueExpression(new IntValue(2))),
                        new PrintStatement(new VariableExpression("v"))));

        IStatement s2 = new CompoundStatement(new VarDeclarationStatement("a", new IntType()),
                new CompoundStatement(new VarDeclarationStatement("b", new IntType()),
                        new CompoundStatement(new AssignStatement("a", new ArithmeticExpression(new ValueExpression(new IntValue(2)), new
                                ArithmeticExpression(new ValueExpression(new IntValue(3)), new ValueExpression(new IntValue(5)), '*'), '+')),
                                new CompoundStatement(new AssignStatement("b", new ArithmeticExpression(new VariableExpression("a"), new ValueExpression(new
                                        IntValue(1)), '+')), new PrintStatement(new VariableExpression("b"))))));

        IStatement s3 = new CompoundStatement(new VarDeclarationStatement("a", new BoolType()),
                new CompoundStatement(new VarDeclarationStatement("v", new IntType()),
                        new CompoundStatement(new AssignStatement("a", new ValueExpression(new BoolValue(true))),
                                new CompoundStatement(new IfStatement(new VariableExpression("a"),
                                        new AssignStatement("v", new ValueExpression(new IntValue(2))),
                                        new AssignStatement("v", new ValueExpression(new IntValue(3)))),
                                        new PrintStatement(new VariableExpression("v"))))));

        IStatement s4 = new CompoundStatement(
                new VarDeclarationStatement("varf", new StringType()),
                new CompoundStatement(
                        new AssignStatement("varf", new ValueExpression(new StringValue("test.in"))),
                        new CompoundStatement(
                                new OpenReadFileStatement(new VariableExpression("varf")),
                                new CompoundStatement(
                                        new VarDeclarationStatement("varc", new IntType()),
                                        new CompoundStatement(
                                                new ReadFileStatement(new VariableExpression("varf"), "varc"),
                                                new CompoundStatement(
                                                        new PrintStatement(new VariableExpression("varc")),
                                                        new CompoundStatement(
                                                                new ReadFileStatement(new VariableExpression("varf"), "varc"),
                                                                new CompoundStatement(
                                                                        new PrintStatement(new VariableExpression("varc")),
                                                                        new CloseReadFileStatement(new VariableExpression("varf"))))))))));

        IStatement s5 = new CompoundStatement(
                new VarDeclarationStatement("v", new RefType(new IntType())),
                new CompoundStatement(
                        new HeapNewStatement("v", new ValueExpression(new IntValue(20))),
                        new CompoundStatement(
                                new VarDeclarationStatement("a", new RefType(new RefType(new IntType()))),
                                new CompoundStatement(
                                        new HeapNewStatement("a", new VariableExpression("v")),
                                        new CompoundStatement(
                                                new PrintStatement(new VariableExpression("v")),
                                                new PrintStatement(new VariableExpression("a")))))));

        IStatement s6 = new CompoundStatement(
                new VarDeclarationStatement("v", new RefType(new IntType())),
                new CompoundStatement(
                        new HeapNewStatement("v", new ValueExpression(new IntValue(20))),
                        new CompoundStatement(
                                new VarDeclarationStatement("a", new RefType(new RefType(new IntType()))),
                                new CompoundStatement(
                                        new HeapNewStatement("a", new VariableExpression("v")),
                                        new CompoundStatement(
                                                new PrintStatement(new HeapReadExpression(new VariableExpression("v"))),
                                                new PrintStatement(new HeapReadExpression(new HeapReadExpression(new VariableExpression("a")))))))));

        IStatement s7 = new CompoundStatement(
                new VarDeclarationStatement("v", new RefType(new IntType())),
                new CompoundStatement(
                        new HeapNewStatement("v", new ValueExpression(new IntValue(20))),
                        new CompoundStatement(
                                new PrintStatement(new HeapReadExpression(new VariableExpression("v"))),
                                new CompoundStatement(
                                        new HeapWriteStatement("v", new ValueExpression(new IntValue(30))),
                                        new PrintStatement(new ArithmeticExpression(new HeapReadExpression(new VariableExpression("v")), new ValueExpression(new IntValue(5)), '+'))))));

        IStatement s8 = new CompoundStatement(
                new VarDeclarationStatement("v", new RefType(new IntType())),
                new CompoundStatement(
                        new HeapNewStatement("v", new ValueExpression(new IntValue(20))),
                        new CompoundStatement(
                                new VarDeclarationStatement("a", new RefType(new RefType(new IntType()))),
                                new CompoundStatement(
                                        new HeapNewStatement("a", new VariableExpression("v")),
                                        new CompoundStatement(
                                                new HeapNewStatement("v", new ValueExpression(new IntValue(30))),
                                                new PrintStatement(new HeapReadExpression(new HeapReadExpression(new VariableExpression("a")))))))));

        IStatement s9 = new CompoundStatement(
                new VarDeclarationStatement("v", new IntType()),
                new CompoundStatement(
                        new AssignStatement("v", new ValueExpression(new IntValue(4))),
                        new CompoundStatement(
                                new WhileStatement(
                                        new RelationalExpression(new VariableExpression("v"), new ValueExpression(new IntValue(0)), ">"),
                                        new CompoundStatement(
                                                new PrintStatement(new VariableExpression("v")),
                                                new AssignStatement("v", new ArithmeticExpression(new VariableExpression("v"), new ValueExpression(new IntValue(1)), '-')))),
                                new PrintStatement(new VariableExpression("v")))));


        IStatement s10 = new CompoundStatement(
                new VarDeclarationStatement("v", new IntType()),
                new CompoundStatement(
                        new VarDeclarationStatement("a", new RefType(new IntType())),
                        new CompoundStatement(
                                new AssignStatement("v", new ValueExpression(new IntValue(10))),
                                new CompoundStatement(
                                        new HeapNewStatement("a", new ValueExpression(new IntValue(22))),
                                        new CompoundStatement(
                                                new ForkStatement(
                                                        new CompoundStatement(
                                                                new HeapWriteStatement("a", new ValueExpression(new IntValue(30))),
                                                                new CompoundStatement(
                                                                        new AssignStatement("v", new ValueExpression(new IntValue(32))),
                                                                        new CompoundStatement(
                                                                                new PrintStatement(new VariableExpression("v")),
                                                                                new PrintStatement(new HeapReadExpression(new VariableExpression("a"))))))),
                                                new CompoundStatement(
                                                        new PrintStatement(new VariableExpression("v")),
                                                        new PrintStatement(new HeapReadExpression(new VariableExpression("a")))))))));


        IStatement s11 = new CompoundStatement(
                new VarDeclarationStatement("a", new RefType(new IntType())),
                new CompoundStatement(new VarDeclarationStatement("v", new IntType()), new CompoundStatement(
                        new HeapNewStatement("a", new ValueExpression(new IntValue(20))),
                        new CompoundStatement(
                                new ForStatement("v",
                                        new ValueExpression(new IntValue(0)),
                                        new ValueExpression(new IntValue(3)),
                                        new ArithmeticExpression(new VariableExpression("v"), new ValueExpression(new IntValue(1)), '+'), //v+1
                                        new ForkStatement(
                                                new CompoundStatement(
                                                        new PrintStatement(new VariableExpression("v")),
                                                        new AssignStatement("v", new ArithmeticExpression(new VariableExpression("v"), new HeapReadExpression(new VariableExpression("a")), '*'))))),
                                new PrintStatement(new HeapReadExpression(new VariableExpression("a")))))));

        IStatement s12 = new CompoundStatement(new VarDeclarationStatement("v1", new RefType(new IntType())),
                new CompoundStatement(new VarDeclarationStatement("v2", new RefType(new IntType())),
                        new CompoundStatement(new VarDeclarationStatement("x", new IntType()),
                                new CompoundStatement(new VarDeclarationStatement("q", new IntType()),
                                        new CompoundStatement(new HeapNewStatement("v1", new ValueExpression(new IntValue(20))),
                                                new CompoundStatement(new HeapNewStatement("v2", new ValueExpression(new IntValue(30))),
                                                        new CompoundStatement(new LockNewStatement("x"),
                                                                new CompoundStatement(new ForkStatement(
                                                                        new CompoundStatement(new ForkStatement(
                                                                                new CompoundStatement(new LockStatement("x"),
                                                                                        new CompoundStatement(new HeapWriteStatement("v1", new ArithmeticExpression(new HeapReadExpression(new VariableExpression("v1")), new ValueExpression(new IntValue(1)), '-')),
                                                                                                new UnlockStatement("x")))
                                                                        ),
                                                                                new CompoundStatement(new LockStatement("x"),
                                                                                        new CompoundStatement(new HeapWriteStatement("v1", new ArithmeticExpression(new HeapReadExpression(new VariableExpression("v1")), new ValueExpression(new IntValue(10)), '*')),
                                                                                                new UnlockStatement("x"))))
                                                                ),
                                                                        new CompoundStatement(new LockNewStatement("q"),
                                                                                new CompoundStatement(new ForkStatement(
                                                                                        new CompoundStatement(new ForkStatement(
                                                                                                new CompoundStatement(new LockStatement("q"),
                                                                                                        new CompoundStatement(new HeapWriteStatement("v2", new ArithmeticExpression(new HeapReadExpression(new VariableExpression("v2")), new ValueExpression(new IntValue(5)), '+')),
                                                                                                                new UnlockStatement("q")))
                                                                                        ),
                                                                                                new CompoundStatement(new LockStatement("q"),
                                                                                                        new CompoundStatement(new HeapWriteStatement("v2", new ArithmeticExpression(new HeapReadExpression(new VariableExpression("v2")), new ValueExpression(new IntValue(10)), '*')),
                                                                                                                new UnlockStatement("q"))))
                                                                                ),
                                                                                        new CompoundStatement(new NoOperationStatement(),
                                                                                                new CompoundStatement(new NoOperationStatement(),
                                                                                                        new CompoundStatement(new NoOperationStatement(),
                                                                                                                new CompoundStatement(new NoOperationStatement(),
                                                                                                                        new CompoundStatement(new LockStatement("x"),
                                                                                                                                new CompoundStatement(new PrintStatement(new HeapReadExpression(new VariableExpression("v1"))),
                                                                                                                                        new CompoundStatement(new UnlockStatement("x"),
                                                                                                                                                new CompoundStatement(new LockStatement("q"),
                                                                                                                                                        new CompoundStatement(new PrintStatement(new HeapReadExpression(new VariableExpression("v2"))),
                                                                                                                                                                new UnlockStatement("q"))))))))))))))))))));


        programStatements = new ArrayList<>(Arrays.asList(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12));
    }

//    private List<String> getStringRepresentations() {
//        return programStatements.stream().map(IStatement::toString).collect(Collectors.toList());
//    }

    @FXML
    public void initialize() {
        buildProgramList();
        programList.setItems(FXCollections.observableArrayList(programStatements));

        displayButton.setOnAction(actionEvent -> {
            int index = programList.getSelectionModel().getSelectedIndex();

            if (index < 0)
                return;

            PrgState initialProgramState = new PrgState(programStatements.get(index));
            IRepository repository = new Repository("logFile" + (index + 1));
            repository.addProgramState(initialProgramState);
            Controller ctrl = new Controller(repository);
            try {
                ctrl.runTypeChecker();
            } catch (Exception e) {
                System.out.println(e.getMessage());
                System.exit(1);
            }
            programController.setController(ctrl);
        });
    }
}