package Model.Expressions;

import Model.DataStructures.IDictionary;
import Model.DataStructures.IHeap;
import Model.Exceptions.EvaluationException;
import Model.Types.IType;
import Model.Values.IValue;


public class VariableExpression implements IExpression {
    private final String var;

    public VariableExpression(String var) {
        this.var = var;
    }

    public String toString() {
        return var;
    }
    @Override
    public IValue eval(IDictionary<String, IValue> tbl, IHeap hp) throws EvaluationException {
        return tbl.get(var);
    }

    public IType typeCheck(IDictionary<String,IType> typeEnv) throws EvaluationException{
        return typeEnv.get(var);
    }

}
