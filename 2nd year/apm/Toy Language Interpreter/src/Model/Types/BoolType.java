package Model.Types;

import Model.Values.BoolValue;
import Model.Values.IValue;

public class BoolType implements IType {
    @Override
    public boolean equals(Object another) {
        return another instanceof BoolType;
    }

    @Override
    public IType getType() {
        return new BoolType();
    }

    @Override
    public IValue getDefault() {
        return new BoolValue(false);
    }

    public String toString() {
        return "boolean";
    }

}
