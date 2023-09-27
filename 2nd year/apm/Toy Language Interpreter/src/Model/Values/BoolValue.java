package Model.Values;

import Model.Types.BoolType;
import Model.Types.IType;

public class BoolValue implements IValue{

    @Override
    public boolean equals(Object obj){
        if(obj instanceof BoolValue castObj) {
            return val == castObj.val;
        }
        return false;
    }
    boolean val;

    public BoolValue(boolean v){
        val=v;
    }

    public boolean getVal() {
        return val;
    }

    public String toString() {
        return ""+val;
    }
    public IType getType() {
        return new BoolType();
    }
}
