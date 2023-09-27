package Model.DataStructures;


import Model.Exceptions.EvaluationException;

import java.util.HashMap;
import java.util.Set;

public interface ILockTable {
    int getFreeValue();

    void put(int key, int value) throws EvaluationException;

    HashMap<Integer, Integer> getContent();

    boolean containsKey(int position);

    int get(int position) throws EvaluationException;

    void update(int position, int value) throws EvaluationException;

    void setContent(HashMap<Integer, Integer> newMap);

    Set<Integer> keySet();
}
