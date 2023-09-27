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

public class UnlockStatement implements IStatement {
    private final String var;
    private static final Lock lock = new ReentrantLock();

    public UnlockStatement(String var) {
        this.var = var;
    }

    @Override
    public PrgState execute(PrgState state) throws EvaluationException {
        lock.lock();
        IDictionary<String, IValue> symTable = state.getSymTable();
        ILockTable lockTable = state.getLockTable();
        if (symTable.isDefined(var)) {
            if (symTable.lookUp(var).getType().equals(new IntType())) {
                IntValue fi = (IntValue) symTable.lookUp(var);
                int foundIndex = fi.getVal();
                if (lockTable.containsKey(foundIndex)) {
                    if (lockTable.get(foundIndex) == state.getId())
                        lockTable.update(foundIndex, -1);
                } else {
                    throw new EvaluationException("Index not in the lock table!");
                }
            } else {
                throw new EvaluationException("Var is not of int type!");
            }
        } else {
            throw new EvaluationException("Variable is not defined!");
        }
        lock.unlock();
        return null;
    }

    @Override
    public IDictionary<String, IType> typeCheck(IDictionary<String, IType> typeEnv) throws EvaluationException {
        if (typeEnv.lookUp(var).equals(new IntType()))
            return typeEnv;
        else
            throw new EvaluationException("Var is not of type int!");
    }


    @Override
    public String toString() {
        return "unlock(" + var + ")";
    }
}
