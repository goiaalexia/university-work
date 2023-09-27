package Model.Values;

import Model.Types.IType;
import Model.Types.RefType;

public class RefValue implements IValue {
    @Override
    public IType getType() {
        return new RefType(locationType);
    }

    public RefValue() {

    }

    public RefValue(int addr, IType locationType) {
        this.address = addr;
        this.locationType = locationType;
    }

    int address;
    IType locationType;

    public int getAddr() {
        return address;
    }

    public IType getLocationType(){
        return locationType;
    }

    @Override
    public String toString() {
        return "ReferenceValue{"+address+" -> "+locationType+"}";
    }


}
