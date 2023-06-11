import React from "react";
import { Chart } from "react-google-charts";

export const data = [
  ["Funds", "per Day"],
  ["Arjun", 11],
  ["Akshay", 2],
  ["Arun", 2],
  ["Adi", 2],
  ["Akash", 7],
];

export const options = {
  title: "Total Fund raise",
};

export default function PieChart() {
  return (
    <Chart
      chartType="PieChart"
      data={data}
      options={options}
      width={"100%"}
      height={"400px"}
    />
  );
}
