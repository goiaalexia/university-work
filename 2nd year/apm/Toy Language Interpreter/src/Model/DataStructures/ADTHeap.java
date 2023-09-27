package Model.DataStructures;

import Model.Exceptions.EvaluationException;
import Model.Exceptions.ExecutionException;
import Model.Values.IValue;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;

// wrapper class used for implementing the heap
public class ADTHeap implements IHeap {
    // memory location -> value kept there
    private final Map<Integer, IValue> map;

    // saving the first next free value
    private Integer freeValue;

    // to generate a random free space in heap memory
    public Integer newValue() {
        Random rand = new Random();
        this.freeValue = Math.abs(rand.nextInt()); // positive number "pointers"

        if (freeValue == 0 || map.containsKey(freeValue)) // null/already generated cases
            freeValue = Math.abs(rand.nextInt());

        return freeValue;
    }


    public ADTHeap(Map<Integer, IValue> map) {
        this.map = map;
        freeValue = newValue();
    }

    public ADTHeap() {
        map = new HashMap<>();
        freeValue = newValue();
    }

    @Override
    public Integer getFreeValue() {
        // threads cannot modify heap at the same time
        synchronized (this) {
            return freeValue;
        }
    }

    @Override
    public Map<Integer, IValue> getContent() {
        synchronized (this) {
            return map;
        }
    }


    @Override
    public void setContent(Map<Integer, IValue> newMap) {
        synchronized (this) {
            map.clear();
            for (Integer i : newMap.keySet()) {
                map.put(i, newMap.get(i));
            }
        }
    }

    @Override
    public Integer add(IValue value) {
        synchronized (this) {
            map.put(freeValue, value);
            Integer freeAddressWhere = freeValue;
            freeValue = newValue();
            return freeAddressWhere;
        }
    }

    @Override
    public void update(Integer position, IValue value) throws ExecutionException {
        synchronized (this) {
            if (!map.containsKey(position))
                throw new ExecutionException(position + " is not a valid position in the heap!");
            map.put(position, value);
        }
    }

    @Override
    public IValue get(Integer position) throws EvaluationException {
        synchronized (this) {
            if (!map.containsKey(position))
                throw new EvaluationException(position + " is not a valid position in the heap!");
            return map.get(position);
        }
    }
}
