import streamlit as st
import math


alphabets = "abcdefghijklmnopqrstuvwhyz"

try:
    st.markdown(":blue[Including numbers will lead unexpected result] ")
    # todo check of init in input
    first_name = st.text_input('Your name, please', '').lower()
    second_name = st.text_input('Your crush\'s name, please', '').lower()

    list_of_ints_in_first = [f"{alphabets.find(c)+1}" for c in first_name]
    list_of_ints_in_second = [f"{alphabets.find(c)+1}" for c in second_name]

    one_leaf = first_name + second_name

    # first, change the letters into init to calculate
    # list of int in str type
    # list_of_ints_in_str = [f"{alphabets.find(c)+1}" for c in one_leaf]
    list_of_ints_in_str = list_of_ints_in_first + list_of_ints_in_second

    # total raw of int, sum of two names
    one_total_str_of_init = "".join(list_of_ints_in_str)

    # only care when appear in both names
    duplicated_init = [
        char for char in list_of_ints_in_str if char in list_of_ints_in_first and char in list_of_ints_in_second]

    # total sum of all two names
    total_of_two = sum([int(i) for i in list_of_ints_in_str])

    # find common's sum
    common_sum = 0
    for i in duplicated_init:
        common_sum = common_sum + int(i)

    # st.write('common_sum ', common_sum)
    # st.write('duplicates_init ', duplicated_init)
    # st.write('leaf_total ', total_of_two)

    # handle zero division error
    handler = 1 if total_of_two == 0 else total_of_two
    final = (common_sum / handler) * 100

    rounded_final = math.floor(final * 100) / 100
#     st.write(f'Chance is: {rounded_final} %')
    st.markdown(f" ## :blue[Chance : {rounded_final} % ] ")

    st.markdown(
        "##### :blue[How it works?]\n  rule : a=1, b=2, c=3, ..., z=26 \n\n  total sum of commom letters / total sum of all the letters in two names")


except:
    st.error("There is an error! Congrats :) ")
