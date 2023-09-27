package Model.Expressions;

import Model.DataStructures.IDictionary;
import Model.DataStructures.IHeap;
import Model.Exceptions.EvaluationException;
import Model.Types.IType;
import Model.Values.IValue;

public class ValueExpression implements IExpression {
    public IValue value;

    public ValueExpression(IValue value) {
        this.value = value;
    }

    @Override
    public String toString() {
        return value.toString();
    }

    @Override
    public IValue eval(IDictionary<String, IValue> tbl, IHeap hp) {
        return value;
    }

    public IType typeCheck(IDictionary<String, IType> typeEnv) {
        return value.getType();
    }
}
