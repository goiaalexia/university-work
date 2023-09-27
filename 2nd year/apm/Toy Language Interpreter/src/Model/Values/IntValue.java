package Model.Values;

import Model.Types.IType;
import Model.Types.IntType;

public class IntValue implements IValue{

    @Override
    public boolean equals(Object obj){
        if(obj instanceof IntValue castObj) {
            return val == castObj.val;
        }
        return false;
    }
    int val;

    public IntValue(int v){
        val=v;
    }

    public int getVal() {
        return val;
    }

    public String toString() {
        return Integer.toString(val);
    }
    public IType getType() {
        return new IntType();
    }
}
