package Model.Statements;

import Model.Exceptions.EvaluationException;
import Model.Exceptions.ExecutionException;
import Model.Expressions.IExpression;
import Model.Expressions.RelationalExpression;
import Model.Expressions.VariableExpression;
import Model.State.PrgState;
import Model.Types.IntType;
import Model.Types.IType;
import Model.DataStructures.IDictionary;
import Model.DataStructures.IStack;

public class ForStatement implements IStatement {
    // v
    private final String variable;
    // v=0
    private final IExpression expression1;
    // v<3
    private final IExpression expression2;
    // v=v+1
    private final IExpression expression3;
    // what shall be executed
    private final IStatement statement;

    public ForStatement(String variable, IExpression expression1, IExpression expression2, IExpression expression3, IStatement statement) {
        this.variable = variable;
        this.expression1 = expression1;
        this.expression2 = expression2;
        this.expression3 = expression3;
        this.statement = statement;
    }

    @Override
    public PrgState execute(PrgState state) throws EvaluationException {
        IStack<IStatement> exeStack = state.getExeStack();
        // we convert it to a compound statement executing with a while equivalent
        IStatement converted = new CompoundStatement(new AssignStatement("v", expression1),
                new WhileStatement(new RelationalExpression(new VariableExpression("v"), expression2, "<"),
                        new CompoundStatement(statement, new AssignStatement("v", expression3))));
        exeStack.push(converted);
        state.exeStack = exeStack;
        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws EvaluationException {

        IType type3 = expression3.typeCheck(typeEnv);
        IType type2 = expression2.typeCheck(typeEnv);
        IType type1 = expression1.typeCheck(typeEnv);

        if (type1.equals(new IntType()) && type2.equals(new IntType()) && type3.equals(new IntType()))
            return typeEnv;
        else
            throw new EvaluationException("For statement failed the type check!");
    }



    @Override
    public String toString() {
        return "for(" + variable + "=" + expression1 + "; " + variable + "<" + expression2 + "; " + variable + "=" + expression3 + ") {" + statement + "}";
    }
}