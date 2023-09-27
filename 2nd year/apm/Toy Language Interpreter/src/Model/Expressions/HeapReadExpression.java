package Model.Expressions;

import Model.DataStructures.IDictionary;
import Model.DataStructures.IHeap;
import Model.Exceptions.EvaluationException;
import Model.Exceptions.ExecutionException;
import Model.Types.IType;
import Model.Types.RefType;
import Model.Values.IValue;
import Model.Values.RefValue;

public class HeapReadExpression implements IExpression {

    private final IExpression expression;

    @Override
    public IValue eval(IDictionary<String, IValue> tbl, IHeap hp) throws EvaluationException {
        IValue evaluated = expression.eval(tbl, hp);
        if (!(evaluated instanceof RefValue referenceValue))
            throw new EvaluationException(evaluated + " is not of type RefType!");

        return hp.get(referenceValue.getAddr());
    }

    @Override
    public IType typeCheck(IDictionary<String, IType> typeEnv) throws EvaluationException {
        IType type= expression.typeCheck(typeEnv);
        if (type instanceof RefType refType) {
            return refType.getInner();
        } else
            throw new EvaluationException("The Heap Read argument is not of type RefType!");
    }



    public HeapReadExpression(IExpression expression) {
        this.expression = expression;
    }

    @Override
    public String toString() {
        return "ReadHeap{"+expression+"}";
    }
}
