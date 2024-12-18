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
