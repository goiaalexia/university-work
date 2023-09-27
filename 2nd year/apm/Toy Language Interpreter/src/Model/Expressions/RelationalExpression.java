package Model.Expressions;

import Model.DataStructures.IDictionary;
import Model.DataStructures.IHeap;
import Model.Exceptions.EvaluationException;
import Model.Types.BoolType;
import Model.Types.IType;
import Model.Types.IntType;
import Model.Values.BoolValue;
import Model.Values.IValue;
import Model.Values.IntValue;

// 5 <= 7
public class RelationalExpression implements IExpression {

    IExpression e1;
    IExpression e2;
    String op; // <=, <, >=, >, ==, !=

    @Override
    public IValue eval(IDictionary<String, IValue> tbl, IHeap hp) throws EvaluationException {
        IValue value1 = e1.eval(tbl, hp);
        IValue value2 = e2.eval(tbl, hp);

        if (!value1.getType().equals(new IntType())) {
            throw new EvaluationException("The first operand of relational expression is not an integer!");
        }
        if (!value2.getType().equals(new IntType())) {
            throw new EvaluationException("The second operand of relational expression is not an integer!");
        }

        IntValue int1 = (IntValue) value1;
        IntValue int2 = (IntValue) value2;

        return switch (op) {
            case "<=" -> new BoolValue(int1.getVal() <= int2.getVal());
            case "<" -> new BoolValue(int1.getVal() < int2.getVal());
            case ">=" -> new BoolValue(int1.getVal() >= int2.getVal());
            case ">" -> new BoolValue(int1.getVal() > int2.getVal());
            case "==" -> new BoolValue(int1.getVal() == int2.getVal());
            case "!=" -> new BoolValue(int1.getVal() != int2.getVal());
            default -> throw new EvaluationException("Invalid relational operator!");
        };
    }

    @Override
    public IType typeCheck(IDictionary<String, IType> typeEnv) throws EvaluationException {
        IType type1, type2;
        type2 = e2.typeCheck(typeEnv);
        type1 = e1.typeCheck(typeEnv);

        if (type1.equals(new IntType())) {
            if (type2.equals(new IntType())) {
                return new BoolType();
            } else
                throw new EvaluationException("Second operand is not an integer!");
        } else
            throw new EvaluationException("First operand is not an integer!");
    }

    public RelationalExpression(IExpression e1, IExpression e2, String op) {
        this.op = op;
        this.e1 = e1;
        this.e2 = e2;

    }

    public String toString() {
        return e1.toString() + op + e2.toString();
    }
}
