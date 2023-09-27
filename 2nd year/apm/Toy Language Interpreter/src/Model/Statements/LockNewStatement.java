package Model.Statements;

import Model.DataStructures.IDictionary;
import Model.DataStructures.ILockTable;
import Model.Exceptions.EvaluationException;
import Model.State.PrgState;
import Model.Types.IType;
import Model.Types.IntType;
import Model.Values.IValue;
import Model.Values.IntValue;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class LockNewStatement implements IStatement {
    private final String var;

    // instantiating using a ReentrantLock
    private static final Lock lock = new ReentrantLock();

    public LockNewStatement(String var) {
        this.var = var;
    }

    @Override
    public PrgState execute(PrgState state) throws EvaluationException {
        // lock the lock
        lock.lock();

        ILockTable lockTable = state.getLockTable();
        IDictionary<String, IValue> symTable = state.getSymTable();
        // find the first free address in the lockTable
        int freeAddress = lockTable.getFreeValue();
        // initialize the lock
        lockTable.put(freeAddress, -1);
        // add it to the symbol table if the variable using the lock exists and is an integer
        if (symTable.isDefined(var) && symTable.lookUp(var).getType().equals(new IntType()))
            symTable.update(var, new IntValue(freeAddress));
        else
            throw new EvaluationException("Variable not declared!");
        lock.unlock();
        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws EvaluationException {
        if (typeEnv.get(var).equals(new IntType()))
            return typeEnv;
        else
            throw new EvaluationException("Variable is not of int type!");
    }

//    @Override
//    public IStatement deepCopy() {
//        return new LockNewStatement(var);
//    }

    @Override
    public String toString() {
        return "newLock(" + var + ")";
    }

}
