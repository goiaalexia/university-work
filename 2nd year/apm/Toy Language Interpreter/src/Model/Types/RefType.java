package Model.Types;

import Model.Values.IValue;
import Model.Values.RefValue;

public class RefType implements IType {

    IType inner;

    @Override
    public IType getType() {
        return new RefType();
    }

    public RefType() {
    }

    @Override
    public IValue getDefault() {
        return new RefValue(0, inner);
    }

    public RefType(IType inner) {this.inner=inner;}

    public IType getInner() {return inner;}

    @Override
    public boolean equals(Object another){
        if (another instanceof  RefType)
            return inner.equals(((RefType) another).getInner());
        else
            return false;
    }

    public String toString() { return "Ref(" +inner.toString()+")";}

    IValue defaultValue() { return new RefValue(0,inner);}


}
