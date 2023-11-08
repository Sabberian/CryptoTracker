import React, { useEffect, useRef } from "react";
import Chart from "chart.js/auto";
import 'chartjs-adapter-moment';

function drawChart(ctx, data) {
    return new Chart(ctx, {
        type: "line",
        data: {
            labels: data.timestamps,
            datasets: [{
                label: "Price",
                data: data.prices,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            scales: {
                x: {
                    type: "time",
                    time: {
                        unit: "hour",
                        stepSize: 1,
                        displayFormats: {
                            hour: "YYYY-MM-DD HH:mm",
                        }
                    },
                    title: {
                        display: true,
                        text: "Date"
                    }
                },
                y: {
                    beginAtZero: false,
                    title: {
                        display: true,
                        text: "Price"
                    }
                }
            }
        }
    });
}

const CryptoChart = ({ data }) => {
    const chartRef = useRef(null);

    console.log(data);

    useEffect(() => {
        if (chartRef.current) {
            const ctx = chartRef.current.getContext("2d");
            drawChart(ctx, data);
        }
    }, [data]);

    return <canvas ref={chartRef} />;
};

export default CryptoChart;