package Model.Values;

import Model.Types.IType;
import Model.Types.StringType;

public class StringValue implements IValue {

    @Override
    public boolean equals(Object obj){
        if(obj instanceof StringValue castObj) {
            return strval.equals(castObj.strval);
        }
        return false;
    }
    public String strval;

    public StringValue(String str) {
        strval = str;
    }

    public String getStrval() {
        return strval;
    }

    @Override
    public String toString() {
        return strval;
    }

    @Override
    public IType getType() {
        return new StringType();
    }
}
