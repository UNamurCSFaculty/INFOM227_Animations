from small.zero_analysis import AbstractZeroAnalysisScene
from small import read_string


class IfInWhileZeroAnalysisScene(AbstractZeroAnalysisScene):
    title = "Zero Analysis of an If Inside a While Loop"

    program = read_string(
        """
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
    )[0]


class SimpleIfZeroAnalysisScene(AbstractZeroAnalysisScene):
    title = "Zero Analysis of a Simple If Statement"

    program = read_string(
        """
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
    )[0]


class SumZeroAnalysisScene(AbstractZeroAnalysisScene):
    title = "Zero Analysis of the Sum Function"

    program = read_string(
        """
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
    )[0]


class NestedIfZeroAnalysisScene(AbstractZeroAnalysisScene):
    title = "Zero Analysis of a Nested If Statement"

    program = read_string(
        """
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
    )[0]
