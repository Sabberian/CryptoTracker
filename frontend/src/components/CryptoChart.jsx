import React, { useEffect, useRef, useState } from "react";
import Chart from "chart.js/auto";
import 'chartjs-adapter-moment';
import ChartMenu from "./ChartMenu";

function createChart(ctx, data) {
    return new Chart(ctx, {
        type: "line",
        data: {
            labels: data.timestamps,
            datasets: [{
                label: data.currency,
                data: data.prices,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            layout: {
                padding: {
                    top: 20,
                    bottom: 10,
                    left: 10,
                    right: 10,
                }
            },
            plugins: {
                legend: {
                    display: false,
                },
                title: {
                    display: true,
                    text: data.currency,
                    font: {
                        size: 18,
                    },
                },
            },
            scales: {
                x: {
                    type: "time",
                    time: {
                        unit: "hour",
                        stepSize: 1,
                        displayFormats: {
                            hour: "MM-DD HH:mm",
                        }
                    },
                },
                y: {
                    beginAtZero: false,
                }
            }
        }
    });
}

const CryptoChart = ({ data }) => {
    const chartRef = useRef(null);
    const chartInstance = useRef(null);
    const [currencyId] = useState(data.currency_id);
    const [direction, setDirection] = useState("up");

    useEffect(() => {
        if (chartRef.current) {
            const ctx = chartRef.current.getContext("2d");
            
            if (!chartInstance.current){
                chartInstance.current = createChart(ctx, data);
            } else {
                chartInstance.current.data.datasets[0].labels = data.labels;
                chartInstance.current.data.datasets[0].data = data.prices;
                chartInstance.current.update();
            }
        }
    }, [data]);

    return (
    <div className="crypto-chart">
        <canvas ref={chartRef} />
            <ChartMenu
                direction={direction}
                setDirection={setDirection}
                currencyId={currencyId}
            />
    </div>
    );
};

export default CryptoChart;