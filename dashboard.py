import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Membaca file CSV
day_df = pd.read_csv("day.csv")

# Buat aggregasi seperti yang Anda lakukan sebelumnya
refered_by_weathersit = (
    day_df.groupby("weathersit").agg({"cnt": ["mean", "min", "max"]}).reset_index()
)

# Rename kolom hasil aggregasi
refered_by_weathersit.columns = ["weathersit", "mean_cnt", "min_cnt", "max_cnt"]

# Title
st.title("Bike Rental Dashboard")

# Dropdown untuk memilih visualisasi
option = st.selectbox(
    "Pilih visualisasi:",
    (
        "Weather with Count",
        "Weather with Registered",
        "Weather with Casual",
        "Weekday with Count",
        "Weekday with Registered",
        "Weekday with Casual",
    ),
)

if option == "Weather with Count":
    st.subheader("Mean, Min, and Max Count of Bike Rentals by Weather Situation")

    # Data untuk plot
    weathersit = refered_by_weathersit["weathersit"]
    mean_cnt = refered_by_weathersit["mean_cnt"]
    min_cnt = refered_by_weathersit["min_cnt"]
    max_cnt = refered_by_weathersit["max_cnt"]

    # Persiapan untuk plotting
    x = np.arange(len(weathersit))
    width = 0.2

    # Membuat figure dan axis
    fig, ax = plt.subplots()

    # Membuat bar chart untuk mean, min, dan max
    ax.bar(x - width, mean_cnt, width, label="Mean", color="skyblue")
    ax.bar(x, min_cnt, width, label="Min", color="lightgreen")
    ax.bar(x + width, max_cnt, width, label="Max", color="salmon")

    # Mengatur label dan title
    ax.set_xlabel("Weather Situation")
    ax.set_ylabel("Count")
    ax.set_title("Mean, Min, and Max of Bike Rentals by Weather Situation")
    ax.set_xticks(x)
    ax.set_xticklabels(weathersit)
    ax.legend()

    # Tampilkan visualisasi di Streamlit
    st.pyplot(fig)

elif option == "Weather with Registered":
    st.subheader("Mean, Min, and Max Registered of Bike Rentals by Weather Situation")

    # Data untuk weekday
    refered_by_weekday = (
        day_df.groupby("weekday")
        .agg({"registered": ["mean", "min", "max"]})
        .reset_index()
    )

    refered_by_weekday.columns = [
        "weekday",
        "mean_registered",
        "min_registered",
        "max_registered",
    ]

    weekday = refered_by_weekday["weekday"]
    mean_registered_weekday = refered_by_weekday["mean_registered"]
    min_registered_weekday = refered_by_weekday["min_registered"]
    max_registered_weekday = refered_by_weekday["max_registered"]

    x = np.arange(len(weekday))
    width = 0.2

    fig, ax = plt.subplots()

    ax.bar(x - width, mean_registered_weekday, width, label="Mean", color="skyblue")
    ax.bar(x, min_registered_weekday, width, label="Min", color="lightgreen")
    ax.bar(x + width, max_registered_weekday, width, label="Max", color="salmon")

    ax.set_xlabel("Weekday")
    ax.set_ylabel("Registered")
    ax.set_title("Mean, Min, and Max of Bike Rentals by Weekday")
    ax.set_xticks(x)
    ax.set_xticklabels(weekday)
    ax.legend()

    # Tampilkan visualisasi di Streamlit
    st.pyplot(fig)

elif option == "Weather with Casual":
    st.subheader("Mean, Min, and Max Casual of Bike Rentals by Weather Situation")

    # Data untuk weekday
    refered_by_weekday = (
        day_df.groupby("weekday").agg({"casual": ["mean", "min", "max"]}).reset_index()
    )

    refered_by_weekday.columns = [
        "weekday",
        "mean_casual",
        "min_casual",
        "max_casual",
    ]

    weekday = refered_by_weekday["weekday"]
    mean_casual_weekday = refered_by_weekday["mean_casual"]
    min_casual_weekday = refered_by_weekday["min_casual"]
    max_casual_weekday = refered_by_weekday["max_casual"]

    x = np.arange(len(weekday))
    width = 0.2

    fig, ax = plt.subplots()

    ax.bar(x - width, mean_casual_weekday, width, label="Mean", color="skyblue")
    ax.bar(x, min_casual_weekday, width, label="Min", color="lightgreen")
    ax.bar(x + width, max_casual_weekday, width, label="Max", color="salmon")

    ax.set_xlabel("Weekday")
    ax.set_ylabel("Casual")
    ax.set_title("Mean, Min, and Max of Bike Rentals by Weekday")
    ax.set_xticks(x)
    ax.set_xticklabels(weekday)
    ax.legend()

    # Tampilkan visualisasi di Streamlit
    st.pyplot(fig)

elif option == "Weekday with Count":
    st.subheader("Mean, Min, and Max Count of Bike Rentals by Weekday")

    # Data untuk weekday
    refered_by_weekday = (
        day_df.groupby("weekday").agg({"cnt": ["mean", "min", "max"]}).reset_index()
    )

    refered_by_weekday.columns = ["weekday", "mean_cnt", "min_cnt", "max_cnt"]

    weekday = refered_by_weekday["weekday"]
    mean_cnt_weekday = refered_by_weekday["mean_cnt"]
    min_cnt_weekday = refered_by_weekday["min_cnt"]
    max_cnt_weekday = refered_by_weekday["max_cnt"]

    x = np.arange(len(weekday))
    width = 0.2

    fig, ax = plt.subplots()

    ax.bar(x - width, mean_cnt_weekday, width, label="Mean", color="skyblue")
    ax.bar(x, min_cnt_weekday, width, label="Min", color="lightgreen")
    ax.bar(x + width, max_cnt_weekday, width, label="Max", color="salmon")

    ax.set_xlabel("Weekday")
    ax.set_ylabel("Count")
    ax.set_title("Mean, Min, and Max of Bike Rentals by Weekday")
    ax.set_xticks(x)
    ax.set_xticklabels(weekday)
    ax.legend()

    # Tampilkan visualisasi di Streamlit
    st.pyplot(fig)

elif option == "Weekday with Registered":
    st.subheader("Mean, Min, and Max Registered of Bike Rentals by Weekday")

    # Data untuk weekday
    refered_by_weekday = (
        day_df.groupby("weekday")
        .agg({"registered": ["mean", "min", "max"]})
        .reset_index()
    )

    refered_by_weekday.columns = [
        "weekday",
        "mean_registered",
        "min_registered",
        "max_registered",
    ]

    weekday = refered_by_weekday["weekday"]
    mean_registered_weekday = refered_by_weekday["mean_registered"]
    min_registered_weekday = refered_by_weekday["min_registered"]
    max_registered_weekday = refered_by_weekday["max_registered"]

    x = np.arange(len(weekday))
    width = 0.2

    fig, ax = plt.subplots()

    ax.bar(x - width, mean_registered_weekday, width, label="Mean", color="skyblue")
    ax.bar(x, min_registered_weekday, width, label="Min", color="lightgreen")
    ax.bar(x + width, max_registered_weekday, width, label="Max", color="salmon")

    ax.set_xlabel("Weekday")
    ax.set_ylabel("Registered")
    ax.set_title("Mean, Min, and Max of Bike Rentals by Weekday")
    ax.set_xticks(x)
    ax.set_xticklabels(weekday)
    ax.legend()

    # Tampilkan visualisasi di Streamlit
    st.pyplot(fig)

elif option == "Weekday with Casual":
    st.subheader("Mean, Min, and Max Casual of Bike Rentals by Weekday")

    # Data untuk weekday
    refered_by_weekday = (
        day_df.groupby("weekday").agg({"casual": ["mean", "min", "max"]}).reset_index()
    )

    refered_by_weekday.columns = ["weekday", "mean_casual", "min_casual", "max_casual"]

    weekday = refered_by_weekday["weekday"]
    mean_casual_weekday = refered_by_weekday["mean_casual"]
    min_casual_weekday = refered_by_weekday["min_casual"]
    max_casual_weekday = refered_by_weekday["max_casual"]

    x = np.arange(len(weekday))
    width = 0.2

    fig, ax = plt.subplots()

    ax.bar(x - width, mean_casual_weekday, width, label="Mean", color="skyblue")
    ax.bar(x, min_casual_weekday, width, label="Min", color="lightgreen")
    ax.bar(x + width, max_casual_weekday, width, label="Max", color="salmon")

    ax.set_xlabel("Weekday")
    ax.set_ylabel("Casual")
    ax.set_title("Mean, Min, and Max of Bike Rentals by Weekday")
    ax.set_xticks(x)
    ax.set_xticklabels(weekday)
    ax.legend()

    # Tampilkan visualisasi di Streamlit
    st.pyplot(fig)
