package Model.Expressions;

import Model.DataStructures.IDictionary;
import Model.DataStructures.IHeap;
import Model.Exceptions.EvaluationException;
import Model.Types.IType;
import Model.Values.IValue;

// expressions
public interface IExpression {
    IValue eval(IDictionary<String,IValue> tbl, IHeap hp) throws EvaluationException;
    IType typeCheck(IDictionary<String,IType> typeEnv) throws EvaluationException;

}
