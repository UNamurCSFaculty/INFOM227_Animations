from small.interval_analysis import AbstractIntervalAnalysisScene
from small.zero_analysis import AbstractZeroAnalysisScene


class IfInWhileZeroAnalysisScene(AbstractZeroAnalysisScene):
    title = "Zero Analysis of an If Inside a While Loop"

    program_string = """
        function main() {
            y = 5 * 2;
            while (x > 0) {
                if (b) {
                    y = x - 2;
                } else {
                    y = x + 2;
                }
            }
            return y;
        }
        """


class SimpleIfZeroAnalysisScene(AbstractZeroAnalysisScene):
    title = "Zero Analysis of a Simple If Statement"

    program_string = """
        function main(a) {
            b = 0 - 5;
            if (b > 0) {
                c = a + 2;
            } else {
                c = b * 2;
            }
            return c;
        }
        """


class UnreachableCodeZeroAnalysisScene(AbstractZeroAnalysisScene):
    title = "Zero Analysis with unreachable code"

    program_string = """
        function main(b) {
            if (False) {
                c = 5;
            } else {
                c = 0;
            }
            return b + c;
        }
        """


class SumZeroAnalysisScene(AbstractZeroAnalysisScene):
    title = "Zero Analysis of the Sum Function"

    program_string = """
        function sum(n) {
            i = 0;
            sum = 0;
            while (i < n) {
                sum = sum + i;
                i = i + 1;
            }
            return sum;
        }
        """


class NestedIfZeroAnalysisScene(AbstractZeroAnalysisScene):
    title = "Zero Analysis of a Nested If Statement"

    program_string = """
        function main() {
            y = 5;
            if (b) {
                if (y > 0) {
                    y = x - 2;
                } else {
                    y = 2 + x;
                }
            } else {}
            return y;
        }
        """


class NestedWhileZeroAnalysisScene(AbstractZeroAnalysisScene):
    title = "Zero Analysis of a Nested While Statement"

    program_string = """
        function main() {
            sum = 0;
            i = 0;
            while (i < 5) {
                j = 0;
                while (j < 5) {
                    sum = sum + 1;
                    j = j + 1;
                }
                i = i + 1;
            }
            return sum;
        }
        """


class ComplexZeroAnalysisScene(AbstractZeroAnalysisScene):
    title = "Zero Analysis of a Complex Program"

    program_string = """
        function main() {
            y = 5;
            if (b) {
                if (y > 0) {
                    y = x - 2;
                    x = 2;
                    while (y > 0) {
                        y = x - 2;
                        y = 2 + x;
                    }
                    y = 5;
                } else {
                    y = 2 + x;
                    while (y > 0) {
                        y = x - 2;
                        y = 2 + x;
                    }
                }
            } else {
                if (y > 0) {
                    y = x - 2;
                    x = 5;
                    x = 6;
                    while (y > 0) {
                        y = x - 2;
                        y = 2 + x;
                    }
                    x = 2;
                } else {
                    y = 2 + x;
                }
            }
            if (y > 0) {
                while (y > 0) {
                    y = x - 2;
                    y = 2 + x;
                }
                y = x - 2;
            } else {
                while (y > 0) {
                    y = x - 2;
                    y = 2 + x;
                    while (y > 0) {
                        y = x - 2;
                        y = 2 + x;
                    }
                }
                y = 2 + x;
            }
            return y;
        }
        """


class FactorialIntervalAnalysisScene(AbstractIntervalAnalysisScene):
    title = "Interval Analysis of the Factorial Function"

    program_string = """
        function fac(n) {
            i = 0;
            f = 1;
            while (i < n) {
                i = i + 1;
                f = f * i;
            }
            return f;
        }
        """
