package Model.Statements;

import Model.DataStructures.IDictionary;
import Model.Exceptions.EvaluationException;
import Model.State.PrgState;
import Model.DataStructures.IStack;
import Model.DataStructures.ADTStack;
import Model.Types.BoolType;
import Model.Types.IType;

public class ForkStatement implements IStatement {
    private final IStatement statement;

    public ForkStatement(IStatement statement) {
        this.statement = statement;
    }

    @Override
    public PrgState execute(PrgState state) {
        IStack<IStatement> newExeStack = new ADTStack<>();
        newExeStack.push(statement);
        return new PrgState(newExeStack, state.getSymTable().copy(),
                state.getOut(), state.getFileTable(), state.getHeap(), state.getLockTable());
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws EvaluationException {
        statement.typeCheck(typeEnv.copy());
        return typeEnv;
    }

    @Override
    public String toString() {
        return "Fork{\n"+statement+"\n}";
    }
}