package Model.Expressions;

import Model.DataStructures.IHeap;
import Model.Exceptions.EvaluationException;
import Model.DataStructures.IDictionary;
import Model.Types.*;
import Model.Values.*;


public class LogicExpression implements IExpression {
    public IExpression e1;

    public IExpression e2;

    String op;

    public LogicExpression(IExpression e1, IExpression e2, String op) {
        this.e1 = e1;
        this.e2 = e2;
        this.op = op;
    }

    @Override
    public IValue eval(IDictionary<String, IValue> symbolTable, IHeap hp) throws EvaluationException {
        IValue value1 = e1.eval(symbolTable, hp);
        IValue value2 = e2.eval(symbolTable, hp);

        if (!value1.getType().equals(new BoolType())) {
            throw new EvaluationException("The first operand is not a boolean value!");
        }
        if (!value2.getType().equals(new BoolType())) {
            throw new EvaluationException("The second operand is not a boolean value!");
        }

        BoolValue bool1 = (BoolValue) value1;
        BoolValue bool2 = (BoolValue) value2;

        return switch (op) {
            case "and" -> new BoolValue(bool1.getVal() && bool2.getVal());
            case "or" -> new BoolValue(bool1.getVal() || bool2.getVal());
            default -> throw new EvaluationException("Invalid boolean operator!");
        };
    }

    public IType typeCheck(IDictionary<String, IType> typeEnv) throws EvaluationException {
        IType type1, type2;
        type1 = e1.typeCheck(typeEnv);
        type2 = e2.typeCheck(typeEnv);

        if (type1.equals(new BoolType())) {
            if (type2.equals(new BoolType())) {
                return new BoolType();
            } else
                throw new EvaluationException("Second operand is not a boolean value!");
        } else
            throw new EvaluationException("First operand is not a boolean value!");
    }

    public String toString() {
        return e1.toString() + " " + op + "  " + e2.toString();
    }

}
