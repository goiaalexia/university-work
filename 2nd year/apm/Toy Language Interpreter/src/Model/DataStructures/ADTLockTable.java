package Model.DataStructures;


import Model.Exceptions.EvaluationException;

import java.util.HashMap;
import java.util.Set;

// synchronized because of sharing
public class ADTLockTable implements ILockTable {
    private HashMap<Integer, Integer> lockTable;
    private int freeLocation = 0;

    public ADTLockTable() {
        this.lockTable = new HashMap<>();

    }

    @Override
    public int getFreeValue() {
        synchronized (this) {
            freeLocation++;
            return freeLocation;
        }
    }

    @Override
    public void put(int key, int value) throws EvaluationException {
        synchronized (this) {
            if (!lockTable.containsKey(key)) {
                lockTable.put(key, value);
            } else {
                throw new EvaluationException("Lock table already contains key" + key + "!");
            }
        }
    }

    @Override
    public HashMap<Integer, Integer> getContent() {
        synchronized (this) {
            return lockTable;
        }
    }

    @Override
    public boolean containsKey(int position) {
        synchronized (this) {
            return lockTable.containsKey(position);
        }
    }

    @Override
    public int get(int position) throws EvaluationException {
        synchronized (this) {
            if (!lockTable.containsKey(position))
                throw new EvaluationException(position + " is not present in the table!");
            return lockTable.get(position);
        }
    }

    @Override
    public void update(int position, int value) throws EvaluationException {
        synchronized (this) {
            if (lockTable.containsKey(position)) {
                lockTable.replace(position, value);
            } else {
                throw new EvaluationException(position + " is not present in the table!");
            }
        }
    }

    @Override
    public void setContent(HashMap<Integer, Integer> newMap) {
        synchronized (this) {
            this.lockTable = newMap;
        }
    }

    @Override
    public Set<Integer> keySet() {
        synchronized (this) {
            return lockTable.keySet();
        }
    }

    @Override
    public String toString() {
        return lockTable.toString();
    }
}
