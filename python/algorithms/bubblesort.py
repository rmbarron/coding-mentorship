#!/usr/bin/python3

"""
A simple sorting algorithm that sorts by "bubbling up" higher integers. Thus, we
end up with a lowest-highest sorted dataset.
"""

def bubblesort(given_list):
  """
  Bubble up higher integers to sort a given list.
  :param given_list: list[int] Integers to be sorted.
  :return: list[int] Sorted list in ascending order.
  """
  completely_sorted = False
  while not completely_sorted:
    update_done = False
    for i in range(1, len(given_list)):
      previous = given_list[i-1]
      if previous > given_list[i]:
        given_list[i-1] = given_list[i]
        given_list[i] = previous
        update_done = True
    if not update_done:
     completely_sorted = True
  return given_list
