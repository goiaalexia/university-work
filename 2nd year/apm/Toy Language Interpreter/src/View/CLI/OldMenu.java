package View.CLI;

import Controller.Controller;
import Model.Exceptions.*;
import Model.Expressions.ArithmeticExpression;
import Model.Expressions.ValueExpression;
import Model.Expressions.VariableExpression;
import Model.Statements.*;
import Model.Types.BoolType;
import Model.Types.IntType;
import Model.Types.StringType;
import Model.Values.BoolValue;
import Model.Values.IntValue;
import Model.Values.StringValue;

import java.util.Scanner;

@Deprecated
public class OldMenu {
    public static void main(String[] args) {
        start();
    }

    public static void start() {
        boolean running = false;
        while (!running) {
            try {
                printMenu();
                Scanner readOption = new Scanner(System.in);
                int option = readOption.nextInt();
                switch (option) {
                    case 1 -> firstExample();
                    case 2 -> secondExample();
                    case 3 -> thirdExample();
                    case 4 -> fourthExample();
                    case 5 -> {
                        running = true;
                        System.out.println("Goodbye!");
                    }
                    default -> System.out.println("Invalid input!");

                }
            } catch (Exception e) {
                System.out.println("\u001B[31m" + e.getMessage() + "\u001B[0m");
            }

        }
    }

    private static void printMenu() {
        System.out.println("MAIN MENU (hardcoded problems)\n1. int v; v=2; Print(v)\n2. int a; int b; a=2+3*5; b=a+1; Print(b)\n3. bool a; int v; a=true; (If a Then v=2 Else v=3); Print(v)\n4. string varf; varf=\"test.in\"; openRFile(varf); int varc; readFile(varf,varc); print(varc); readFile(varf,varc); print(varc); closeRFile(varf)\n5. Exit\nOption: ");
    }

    /* int v; v=2; Print(v) */
    private static void firstExample() throws EvaluationException, ExecutionException, ListException, DictionaryException, StackException {
        IStatement statement = new CompoundStatement(new VarDeclarationStatement("v", new IntType()),
                new CompoundStatement(new AssignStatement("v", new ValueExpression(new IntValue(2))),
                        new PrintStatement(new VariableExpression("v"))));
        runStatement(statement);
    }

    /* int a; int b; a=2+3*5; b=a+1; Print(b) */
    private static void secondExample() throws EvaluationException, ExecutionException, ListException, DictionaryException, StackException {
        IStatement statement = new CompoundStatement(new VarDeclarationStatement("a", new IntType()),
                new CompoundStatement(new VarDeclarationStatement("b", new IntType()),
                        new CompoundStatement(new AssignStatement("a", new ArithmeticExpression(new ValueExpression(new IntValue(2)), new
                                ArithmeticExpression(new ValueExpression(new IntValue(3)), new ValueExpression(new IntValue(5)), '*'), '+')),
                                new CompoundStatement(new AssignStatement("b", new ArithmeticExpression(new VariableExpression("a"), new ValueExpression(new
                                        IntValue(1)), '+')), new PrintStatement(new VariableExpression("b"))))));
        runStatement(statement);
    }

    /* bool a; int v; a=true; (If a Then v=2 Else v=3); Print(v) */
    private static void thirdExample() throws EvaluationException, ExecutionException, ListException, DictionaryException, StackException {
        IStatement statement = new CompoundStatement(new VarDeclarationStatement("a", new BoolType()),
                new CompoundStatement(new VarDeclarationStatement("v", new IntType()),
                        new CompoundStatement(new AssignStatement("a", new ValueExpression(new BoolValue(true))),
                                new CompoundStatement(new IfStatement(new VariableExpression("a"),
                                        new AssignStatement("v", new ValueExpression(new IntValue(2))),
                                        new AssignStatement("v", new ValueExpression(new IntValue(3)))),
                                        new PrintStatement(new VariableExpression("v"))))));
        runStatement(statement);
    }

    private static void fourthExample() throws EvaluationException, ExecutionException, DictionaryException, StackException {
        IStatement statement = new CompoundStatement(
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
        runStatement(statement);
    }

    private static void runStatement(IStatement statement) throws
            EvaluationException, ExecutionException, DictionaryException, StackException {
        Controller controller = new Controller("C:\\Users\\lexig\\IdeaProjects\\a3\\logFile", false);
        controller.addProgram(statement);
        if (controller.stepByStep) {
            controller.stepByStepExecution();
        } else {
            controller.executeAllSteps();
        }
        System.out.println("Result: " + controller.getRepository().getCurrentProgramState().outToString());
    }
}
