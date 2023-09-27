package View.CLI;

import Controller.Controller;
import Model.Expressions.*;
import Model.Statements.*;
import Model.Types.BoolType;
import Model.Types.IntType;
import Model.Types.RefType;
import Model.Types.StringType;
import Model.Values.BoolValue;
import Model.Values.IntValue;
import Model.Values.StringValue;
import View.CLI.TextMenu;
import View.Commands.ExitCommand;
import View.Commands.RunCommand;

import java.io.IOException;

public class View {

    public static void main(String[] args) throws IOException {
        TextMenu menu = new TextMenu();

        Controller c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12;

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
                new CompoundStatement( new VarDeclarationStatement("v", new IntType()), new CompoundStatement(
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
        c1 = new Controller("C:\\Users\\lexig\\IdeaProjects\\a3\\logFile1", false);
        c2 = new Controller("C:\\Users\\lexig\\IdeaProjects\\a3\\logFile2", false);
        c3 = new Controller("C:\\Users\\lexig\\IdeaProjects\\a3\\logFile3", false);
        c4 = new Controller("C:\\Users\\lexig\\IdeaProjects\\a3\\logFile4", false);
        c5 = new Controller("C:\\Users\\lexig\\IdeaProjects\\a3\\logFile5", false);
        c6 = new Controller("C:\\Users\\lexig\\IdeaProjects\\a3\\logFile6", false);
        c7 = new Controller("C:\\Users\\lexig\\IdeaProjects\\a3\\logFile7", false);
        c8 = new Controller("C:\\Users\\lexig\\IdeaProjects\\a3\\logFile8", false);
        c9 = new Controller("C:\\Users\\lexig\\IdeaProjects\\a3\\logFile9", false);
        c10 = new Controller("C:\\Users\\lexig\\IdeaProjects\\a3\\logFile10", true);
        c11 = new Controller("C:\\Users\\lexig\\IdeaProjects\\a3\\logFile11", false);
        c12 = new Controller("C:\\Users\\lexig\\IdeaProjects\\a3\\logFile12", false);

        c1.addProgram(s1);
        c2.addProgram(s2);
        c3.addProgram(s3);
        c4.addProgram(s4);
        c5.addProgram(s5);
        c6.addProgram(s6);
        c7.addProgram(s7);
        c8.addProgram(s8);
        c9.addProgram(s9);
        c10.addProgram(s10);
        c11.addProgram(s11);
        c12.addProgram(s12);

        RunCommand r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12;

        r1 = new RunCommand(s1, "1", "int v; v=2; Print(v)", c1);
        r2 = new RunCommand(s2, "2", "int a; int b; a=2+3*5; b=a+1; Print(b)", c2);
        r3 = new RunCommand(s3, "3", "bool a; int v; a=true; (If a Then v=2 Else v=3); Print(v)", c3);
        r4 = new RunCommand(s4, "4", "string varf; varf=\"test.in\"; openReadFile(varf); int varc; readFile(varf,varc); print(varc); readFile(varf,varc); print(varc); closeReadFile(varf)", c4);
        r5 = new RunCommand(s5, "5", "Ref int v;new(v,20);Ref Ref int a; new(a,v);print(v);print(a)", c5);
        r6 = new RunCommand(s6, "6", "Ref int v;new(v,20);Ref Ref int a; new(a,v);print(rH(v));print(rH(rH(a)))", c6);
        r7 = new RunCommand(s7, "7", "Ref int v;new(v,20);print(rH(v)); wH(v,30);print(rH(v)+5);", c7);
        r8 = new RunCommand(s8, "8", "Ref int v;new(v,20);Ref Ref int a; new(a,v); new(v,30);print(rH(rH(a)))", c8);
        r9 = new RunCommand(s9, "9", "int v; v=4; (while (v>0) print(v);v=v-1);print(v)", c9);
        r10 = new RunCommand(s10, "10", "int v; Ref int a; v=10; new(a,22); fork(wH(a,30);v=32;print(v);print(rH(a)));print(v);print(rH(a))", c10);
        r11 = new RunCommand(s11, "11", "Ref int a; new(a,20);(for(v=0;v<3;v=v+1) fork(print(v);v=v*rh(a)));print(rh(a))", c11);
        r12 = new RunCommand(s12, "12", "lock example", c12);
        menu.addCommand(r1);
        menu.addCommand(r2);
        menu.addCommand(r3);
        menu.addCommand(r4);
        menu.addCommand(r5);
        menu.addCommand(r6);
        menu.addCommand(r7);
        menu.addCommand(r8);
        menu.addCommand(r9);
        menu.addCommand(r10);
        menu.addCommand(r11);
        menu.addCommand(r12);

        menu.addCommand(new ExitCommand("13", "Exit"));
        menu.show();
    }

}