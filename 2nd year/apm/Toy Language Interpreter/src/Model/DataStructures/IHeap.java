package Model.DataStructures;

import Model.Exceptions.EvaluationException;
import Model.Exceptions.ExecutionException;
import Model.Values.IValue;

import java.util.Map;

public interface IHeap {
    Integer getFreeValue();

    Map<Integer, IValue> getContent();

    void setContent(Map<Integer, IValue> newMap);

    Integer add(IValue value);

    void update(Integer position, IValue value) throws ExecutionException;

    IValue get(Integer position) throws EvaluationException;
}