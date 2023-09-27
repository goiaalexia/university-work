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

public class LockStatement implements IStatement {
    private final String var;
    private static final Lock lock = new ReentrantLock();

    public LockStatement(String var) {
        this.var = var;
    }

    @Override
    public PrgState execute(PrgState state) throws EvaluationException {
        // lock the lock
        lock.lock();
        IDictionary<String, IValue> symTable = state.getSymTable();
        ILockTable lockTable = state.getLockTable();
        // if the variable exists and is int
        if (symTable.isDefined(var)) {
            if (symTable.lookUp(var).getType().equals(new IntType())) {
                // we get its value and search for it in the lockTable
                IntValue fi = (IntValue) symTable.lookUp(var);
                int foundIndex = fi.getVal();
                if (lockTable.containsKey(foundIndex)) {
                    // we lock it for the program state that is running
                    if (lockTable.get(foundIndex) == -1) {
                        lockTable.update(foundIndex, state.getId());
                        state.lockTable = lockTable;
                    } else {
                        state.getExeStack().push(this);
                    }
                } else {
                    throw new EvaluationException("Index is not in the lock table!");
                }
            } else {
                throw new EvaluationException("Var is not of type int!");
            }
        } else {
            throw new EvaluationException("Variable not defined!");
        }
        lock.unlock();
        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws EvaluationException {
        if (typeEnv.lookUp(var).equals(new IntType())) {
            return typeEnv;
        } else {
            throw new EvaluationException("Var is not of int type!");
        }
    }



    @Override
    public String toString() {
        return "lock(" + var + ")";
    }
}
