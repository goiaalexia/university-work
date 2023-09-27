package Model.Statements;

import Model.DataStructures.IDictionary;
import Model.DataStructures.IStack;
import Model.Exceptions.EvaluationException;
import Model.State.PrgState;
import Model.Types.IType;

// plenty of them
public class CompoundStatement implements IStatement {
    IStatement first;
    IStatement second;

    @Override
    public String toString() {
        return "(" + first.toString() + ";" + second.toString() + ")";
    }

    public CompoundStatement(IStatement first, IStatement second) {
        this.first = first;
        this.second = second;
    }

    @Override
    public PrgState execute(PrgState state) {
        IStack<IStatement> stack = state.getExeStack();
        stack.push(second);
        stack.push(first);
        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws EvaluationException {
        // IDictionary<String,IType> typeEnv1 = first.typeCheck(typeEnv);
        // IDictionary<String,IType> typeEnv2 = second.typeCheck(typeEnv1);
        // return typeEnv2;
        return second.typeCheck(first.typeCheck(typeEnv));
    }
}
