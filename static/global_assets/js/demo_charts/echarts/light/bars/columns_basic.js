/* ------------------------------------------------------------------------------
 *
 *  # Echarts - Basic column example
 *
 *  Demo JS code for basic column chart [light theme]
 *
 * ---------------------------------------------------------------------------- */


// Setup module
// ------------------------------
// Day, Month, Year Filters


var check = 'M';

var mainDashboardChart = async function () {
    const response = await fetch(`http://127.0.0.1:8000/attendance_record_service/${check}`);
    // waits until the request completes...

    var apiData = 0;
    response.json().then(function(data) {
        // console.log();
        apiData = data.map((item) => {return JSON.parse(item)})
        var _columnsBasicLightExample = function () {
            if (typeof echarts == 'undefined') {
                console.warn('Warning - echarts.min.js is not loaded.');
                return;
            }
        
            // Define element
            var columns_basic_element = document.getElementById('columns_basic');
        
        
            //
            // Charts configuration
            //
            console.log(apiData.map((item) => {return Object.values(item)[0]['p']}));
        
            if (columns_basic_element) {
        
                // Initialize chart
                var columns_basic = echarts.init(columns_basic_element);
        
        
                //
                // Chart config
                //
        
                // Options
                console.log('APIDATA', apiData)
                columns_basic.setOption({
        
                    // Define colors
                    color: ['#2ec7c9', '#b6a2de', '#5ab1ef', '#ffb980', '#d87a80'],
        
                    // Global text styles
                    textStyle: {
                        fontFamily: 'Roboto, Arial, Verdana, sans-serif',
                        fontSize: 13
                    },
        
                    // Chart animation duration
                    animationDuration: 750,
        
                    // Setup grid
                    grid: {
                        left: 0,
                        right: 40,
                        top: 35,
                        bottom: 0,
                        containLabel: true
                    },
        
                    // Add legend
                    legend: {
                        data: ['Evaporation', 'Precipitation'],
                        itemHeight: 8,
                        itemGap: 20,
                        textStyle: {
                            padding: [0, 5]
                        }
                    },
        
                    // Add tooltip
                    tooltip: {
                        trigger: 'axis',
                        backgroundColor: 'rgba(0,0,0,0.75)',
                        padding: [10, 15],
                        textStyle: {
                            fontSize: 13,
                            fontFamily: 'Roboto, sans-serif'
                        }
                    },
        
                    // Horizontal axis
                    xAxis: [{
                        type: 'category',
                        // data: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                        data: apiData.map((item) => {return Object.keys(item)}),
                        axisLabel: {
                            color: '#333'
                        },
                        axisLine: {
                            lineStyle: {
                                color: '#999'
                            }
                        },
                        splitLine: {
                            show: true,
                            lineStyle: {
                                color: '#eee',
                                type: 'dashed'
                            }
                        }
                    }],
        
                    // Vertical axis
                    yAxis: [{
                        type: 'value',
                        axisLabel: {
                            color: '#333'
                        },
                        axisLine: {
                            lineStyle: {
                                color: '#999'
                            }
                        },
                        // splitLine: {
                        //     lineStyle: {
                        //         color: ['#eee']
                        //     }
                        // },
                        // splitArea: {
                        //     show: true,
                        //     areaStyle: {
                        //         color: ['rgba(250,250,250,0.1)', 'rgba(0,0,0,0.01)']
                        //     }
                        // }
                    }],
        
                    // Add series
                    series: [
                        {
                            name: 'P',
                            type: 'bar',
                            data: apiData.map((item) => {return Object.values(item)[0]['p']}),
                            itemStyle: {
                                normal: {
                                    label: {
                                        show: true,
                                        position: 'top',
                                        textStyle: {
                                            fontWeight: 500
                                        }
                                    }
                                }
                            }
                        },
                        {
                            name: 'OF',
                            type: 'bar',
                            data: apiData.map((item) => {return Object.values(item)[0]['of']}),
                            itemStyle: {
                                normal: {
                                    label: {
                                        show: true,
                                        position: 'top',
                                        textStyle: {
                                            fontWeight: 500
                                        }
                                    }
                                }
                            }
                        },
                        {
                            name: 'SL',
                            type: 'bar',
                            data: apiData.map((item) => {return Object.values(item)[0]['sl']}),
                            itemStyle: {
                                normal: {
                                    label: {
                                        show: true,
                                        position: 'top',
                                        textStyle: {
                                            fontWeight: 500
                                        }
                                    }
                                }
                            }
                        },
                        {
                            name: 'AL',
                            type: 'bar',
                            data: apiData.map((item) => {return Object.values(item)[0]['al']}),
                            itemStyle: {
                                normal: {
                                    label: {
                                        show: true,
                                        position: 'top',
                                        textStyle: {
                                            fontWeight: 500
                                        }
                                    }
                                }
                            }
                        },
                        {
                            name: 'OW',
                            type: 'bar',
                            data: apiData.map((item) => {return Object.values(item)[0]['ow']}),
                            itemStyle: {
                                normal: {
                                    label: {
                                        show: true,
                                        position: 'top',
                                        textStyle: {
                                            fontWeight: 500
                                        }
                                    }
                                }
                            }
                        },
                        {
                            name: 'X',
                            type: 'bar',
                            data: apiData.map((item) => {return Object.values(item)[0]['x']}),
                            itemStyle: {
                                normal: {
                                    label: {
                                        show: true,
                                        position: 'top',
                                        textStyle: {
                                            fontWeight: 500
                                        }
                                    }
                                }
                            }
                        },
                        {
                            name: 'UP',
                            type: 'bar',
                            data: apiData.map((item) => {return Object.values(item)[0]['up']}),
                            itemStyle: {
                                normal: {
                                    label: {
                                        show: true,
                                        position: 'top',
                                        textStyle: {
                                            fontWeight: 500
                                        }
                                    }
                                }
                            }
                        },
                        {
                            name: 'WC',
                            type: 'bar',
                            data: apiData.map((item) => {return Object.values(item)[0]['wc']}),
                            itemStyle: {
                                normal: {
                                    label: {
                                        show: true,
                                        position: 'top',
                                        textStyle: {
                                            fontWeight: 500
                                        }
                                    }
                                }
                            }
                        },
                    ]
                });
            }
        
        
            //
            // Resize charts
            //
        
            // Resize function
            var triggerChartResize = function () {
                columns_basic_element && columns_basic.resize();
            };
        
            // On sidebar width change
            var sidebarToggle = document.querySelectorAll('.sidebar-control');
            if (sidebarToggle) {
                sidebarToggle.forEach(function (togglers) {
                    togglers.addEventListener('click', triggerChartResize);
                });
            }
        
            // On window resize
            var resizeCharts;
            window.addEventListener('resize', function () {
                clearTimeout(resizeCharts);
                resizeCharts = setTimeout(function () {
                    triggerChartResize();
                }, 200);
            });
        };
        
        
        //
        // Return objects assigned to module
    
        // response.then((res) => console.log(res));
        return _columnsBasicLightExample();
    });


    // return {
    //     init: function () {
    //         _columnsBasicLightExample();
    //     }
    // }
}

var EchartsColumnsBasicLight = function () {


    //
    // Setup module components
    //


}();

function updateChck(param) {
    console.log('clicked')
    check = param
    mainDashboardChart();
}
  
// document.getElementById('main-dash-y').addEventListener("click", updateChck('Y'));
// document.getElementById('main-dash-m').addEventListener("click", updateChck('M'));
// document.getElementById('main-dash-d').addEventListener("click", updateChck('D'));
// Initialize module
// ------------------------------

document.addEventListener('DOMContentLoaded', function () {
    mainDashboardChart();
    // EchartsColumnsBasicLight.init();
});
