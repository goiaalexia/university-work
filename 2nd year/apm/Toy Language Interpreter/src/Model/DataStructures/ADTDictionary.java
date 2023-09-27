package Model.DataStructures;

import Model.Exceptions.EvaluationException;

import java.util.Enumeration;
import java.util.Hashtable;
import java.util.Map;

// wrapper class used by the file & symbol tables.
public class ADTDictionary<k, v> implements IDictionary<k, v> {

    Hashtable<k, v> data = new Hashtable<>();

    @Override
    public boolean isDefined(k key) {
        synchronized (this) {
            return this.data.containsKey(key);
        }
    }

    @Override
    public void update(k key, v value) throws EvaluationException {
        synchronized (this) {
            if (!isDefined(key))
                throw new EvaluationException(key + " is not defined.");
            this.data.put(key, value);
        }
    }

    @Override
    public v lookUp(k key) throws EvaluationException {
        synchronized (this) {
            if (!isDefined(key))
                throw new EvaluationException(key + " is not defined.");
            return this.data.get(key);
        }
    }
    @Override
    public int size() {synchronized(this){
        return data.size();
    }}

    @Override
    public boolean isEmpty() {
        return data.isEmpty();
    }

    @Override
    public Enumeration<k> keys() {
        synchronized (this) {
            return data.keys();
        }
    }

    @Override
    public Enumeration<v> elements() {synchronized (this){
        return data.elements();
    }}

    @Override
    public v get(k key) {synchronized (this){
        return data.get(key);
    }}

    @Override
    public v put(k key, v value) {synchronized (this){
        return data.put(key, value);}
    }

    @Override
    public v remove(k key) {synchronized (this){
        return data.remove(key);
    }}

    @Override
    public boolean containsKey(k id) {synchronized (this){
        return data.containsKey(id);
    }}

    @Override
    public IDictionary<k, v> copy() {synchronized (this){
        IDictionary<k, v> toReturn = new ADTDictionary<>();
        for (k key : data.keySet())
            toReturn.put(key, get(key));
        return toReturn;
    }}

    @Override
    public Map<k, v> getContent() {synchronized (this){
        return data;
    }}


}
