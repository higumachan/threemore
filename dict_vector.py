#coding: utf-8

from copy import deepcopy
import cmath

class DictVector(dict):
    def __add__(self, other):
        result = deepcopy(self);
        for k, v in other.items():
            if (result.has_key(k)):
                result[k] += v;
            else:
                result[k] = v;
        return result;
    def __sub__(self, other):
        result = deepcopy(self);
        for k, v in other.items():
            if (result.has_key(k)):
                result[k] -= v;
            else:
                result[k] = -v;
        return result;
    def __mul__(self, other):
        result = None;
        if (type(other) == int):
            result = deepcopy(self);
            for k in result.keys():
                result[k] *= other;
        else:
            result = 0;
            for k, v in other.items():
                if (self.has_key(k)):
                    result += v * self[k];
        return result;

    def __div__(self, other):
        result = deepcopy(self);
        for k in result.keys():
            result[k] /= other;
        return result;

    def size_sqr(self):
        result = 0;
        for v in self.values():
            result += v * v;
        return result;

    def size(self):
        return cmath.sqrt(self.size_sqr()).real;

    def nomalize(self):
        size = self.size();
        for k in self.keys():
            self[k] /= size;

    def get_nomal(self):
        size = self.size();
        return self / size;
    
    def average(self):
        values = self.values();
        return sum(values) / len(values);
    
    def get_distribution_vector(self):
        average = self.average();
        return {k: v - average for k, v in self.items()};
    
    def get_deviation_vector(self, other):
        return (self + other) / 2.0;

if __name__ == "__main__":
    dv1 = DictVector({"a": 1, "b": 2});
    dv2 = DictVector({"c": 1, "a": 2});
    print dv1 + dv2;
    print dv1 - dv2;
    print dv1 * 2;
    print dv1 * dv2;
    print dv1.size();
    dv1.nomalize();
    print dv1
    print dv1.size()

