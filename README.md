# Sorting
[![](https://github.com/buffeinstein/sorting-cs46hw04/workflows/tests/badge.svg)](https://github.com/buffeinstein/sorting-cs46hw04/actions?query=workflow%3Atests)
[![](https://github.com/mikeizbicki/sorting/workflows/extra_credit/badge.svg)](https://github.com/mikeizbicki/sorting/actions?query=workflow%3Atests)

You will implement the merge and quick sort algorithms.

**Learning Objectives:**

1. understand how merge sort and quicksort work
1. practice recursion
1. practice using property-based tests

**Real-world application:**

Given a dataset, the first step of processing is almost always to sort the data.
This allows efficient lookups via binary search,
but it even makes sequential search significantly faster due to an optimization in modern CPUs called "branch prediction".
(See [the most upvoted stackoverflow question of all time](https://stackoverflow.com/questions/11227809/why-is-processing-a-sorted-array-faster-than-processing-an-unsorted-array) for details.)
Technical interviews therefore often require you to explain how the merge and quicksort algorithms work.

> **ASIDE:**
> Recall that Python uses the [TimSort](https://en.wikipedia.org/wiki/Timsort) algorithm.
> TimSort was named after the inventor [Tim Peters](https://en.wikipedia.org/wiki/Tim_Peters_(software_engineer\)),
> who invented it specifically for python.
> Tim is one of the most influential early python programmers after Python's [BDFL](https://en.wikipedia.org/wiki/Benevolent_dictator_for_life) [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum).
> Besides TimSort, he is most famous for developing the [Zen of Python](https://en.wikipedia.org/wiki/Zen_of_Python),
> which is a collection of sayings describing python's guiding philosophy.
> You can access the Zen of Python from within python by running the command
> ```
> >>> import this
> ```

In the real world, you should never implement your own sorting algorithm.
The algorithms built-in to standard libraries are highly optimized by highly skilled engineers,
and therefore will be much faster than anything you are likely to write.

So why are you implementing them in this assignment?
The divide-and-conquer strategy used in merge/quick sort turns out to be the most fundamental tool for building your own fast algorithms,
and the main purposee of this assignment is to practice this divde-and-conquer programming technique.
Next week, we will explore this strategy for massively parallel data analysis of multi-terabyte twitter data.
If you take CS148 (graph algorithms), you will explore many more variations of the divide and conquer technique for developing fast algorithms.
Data science tasks frequently rely on matrix multiplication and the fourier transform,
and the fastest versions of these algorithms are implemented via divide and conquer.

## Tasks

Complete the following tasks:

1. Fork the [sorting repo](https://github.com/mikeizbicki/sorting) and enable github actions
1. Update the `README.md` file so that the test case badges point to your repo.
1. Implement the `_merged`, `merge_sorted`, and `quick_sorted` functions so that all test cases in `tests/test_main.py` pass.
   You must implement `merge_sorted` and `quick_sorted` recursively.
1. (optionally)
   You can receive 1 point of extra credit for implementing the `quick_sort` function and passing the tests in `tests/test_ec.py`.

## Submission

Submit the link to your forked repository on sakai.
