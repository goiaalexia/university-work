package Model.Statements;

import Model.DataStructures.IDictionary;
import Model.Exceptions.EvaluationException;
import Model.State.PrgState;
import Model.Types.IType;

public class NoOperationStatement implements IStatement{

    @Override
    public PrgState execute(PrgState state) {
        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws EvaluationException {
        return typeEnv;
    }

    @Override
    public String toString() {
        return "no operation";
    }
}
