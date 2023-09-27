package Model.Types;

import Model.Values.IValue;
import Model.Values.IntValue;

public class IntType implements IType {
    @Override
    public boolean equals(Object another) {
        return another instanceof IntType;
    }

    public IntType() {
    }

    public IType getType() {
        return new IntType();
    }
    @Override
    public IValue getDefault() {
        return new IntValue(0);
    }

    public String toString() {
        return "int";
    }
}
