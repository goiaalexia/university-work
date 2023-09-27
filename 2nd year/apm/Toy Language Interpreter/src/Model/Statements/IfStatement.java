package Model.Statements;

import Model.DataStructures.IDictionary;
import Model.Exceptions.EvaluationException;
import Model.Exceptions.ExecutionException;
import Model.Expressions.IExpression;
import Model.State.PrgState;
import Model.Types.BoolType;
import Model.Types.IType;
import Model.Values.BoolValue;
import Model.Values.IValue;

public class IfStatement implements IStatement {
    private final IExpression exp; // condition
    private final IStatement thenS;
    private final IStatement elseS;

    public IfStatement(IExpression exp, IStatement thenS, IStatement elseS) {
        this.exp = exp;
        this.thenS = thenS;
        this.elseS = elseS;
    }

    @Override
    public PrgState execute(PrgState state) throws EvaluationException, ExecutionException {
        IValue value = exp.eval(state.getSymTable(), state.getHeap());

        if (!value.getType().equals(new BoolType())) {
            throw new EvaluationException(String.format("Condition %s is not of type bool, therefore it can't be evaluated!", value));
        }

        BoolValue condition = (BoolValue) value;
        if (condition.getVal()) {
            state.getExeStack().push(thenS);
        } else {
            state.getExeStack().push(elseS);
        }
        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws EvaluationException {
        IType typeExpression = exp.typeCheck(typeEnv);
        if (typeExpression.equals(new BoolType())) {
            thenS.typeCheck(typeEnv.copy());
            elseS.typeCheck(typeEnv.copy());
            return typeEnv;
        }
        else
            throw new EvaluationException("The condition of the if statement is not of type BoolType!");
    }

    @Override
    public String toString() {
        return String.format("if(%s) then(%s) else(%s)", exp.toString(), thenS.toString(), elseS.toString());
    }
}
