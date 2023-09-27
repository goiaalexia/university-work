package Model.Types;

import Model.Values.IValue;

// used for assignments, because we need the variable type
public interface IType {
    IType getType();
    IValue getDefault();

}
