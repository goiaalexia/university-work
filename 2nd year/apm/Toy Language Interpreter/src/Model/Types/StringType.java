package Model.Types;

import Model.Values.IValue;
import Model.Values.StringValue;

public class StringType implements IType{
    @Override
    public boolean equals(Object another) {
        return another instanceof StringType;
    }

    public StringType(){

    }

    @Override
    public IType getType() {
        return new StringType();
    }

    @Override
    public IValue getDefault() {
        return new StringValue(" ");
    }

    @Override
    public String toString() {
        return "String";
    }
}
