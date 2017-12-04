import multiprocessing
import time

from influxdb import InfluxDBClient

jsonbody = [
    {
        "measurement": "mesosstats",
        "tags": {

            "app": "vega-web",
            "cmd": "c2VsZWN0",
            "host": "a6",
            "hostname": "runtimes_open-sourcepampas-blog_dev_develop_blog-service.0d27aca0-77fb-11e7-ad1a-70b3d5800001",
            "metric_type": "timing",
            "name": "Blog.list",
            "service": "terminus-servlet",
            "source": "spring",
            "sql": "select * from test",
            "terminus_key": "0ced984094e911e6806da0d3c1f20c44",
            "terminusKey": "69ff797c59dc4f6f9981e3fc7c1a3597"

        },
        "fields": {
            "75_percentile": 1446,
            "95_percentile": 1454,
            "count": 10,
            "lower": 1439.0,
            "mean": 1444.6,
            "stddev": 3.8522720568516444,
            "upper": 1454
        }
    }
]

jsonbody_servlets = [
    {
        "measurement": "mesosstats",
        "tags": {
            "host": "master",
            "server": "master.mesos",
            "terminusKey": ""
        },
        "fields": {
            "TASK_ERROR": 0,
            "TASK_FAILED": 984,
            "TASK_FINISHED": 0,
            "TASK_KILLED": 16,
            "TASK_KILLING": 0,
            "TASK_LOST": 0,
            "TASK_RUNNING": 204,
            "TASK_STAGING": 0,
            "TASK_STARTING": 0,
            "TASK_UNREACHABLE": 59,
            "agent_total": 10,
            "cpu_used_rate": 0.85614,
            "cpus": 44,
            "cpus_used": 37.67,
            "disk": 1326674,
            "disk_used": 6032,
            "disk_used_rate": 0.00455,
            "gpus": 0,
            "gpus_used": 0,
            "gpus_used_rate": 0,
            "health_agents": "10.0.2.155,10.0.2.154,10.0.2.141,10.0.2.150,10.0.2.148,10.0.2.144,10.0.2.142,"
                             "10.0.2.143,10.0.2.158,10.0.2.157",
            "health_agents_num": "10",
            "health_masters": "10.0.2.147",
            "health_masters_num": 1,
            "health_public_agents": "10.0.2.146,10.0.2.145",
            "health_public_agents_num": 2,
            "master_total": 1,
            "mem": "151324",
            "mem_used": "129574",
            "mem_used_rate": "0.85627",
            "public_agent_total": 2,
            "unhealth_agents": "",
            "unhealth_masters": "",
            "unhealth_public_agents": ""
        }
    }
]

jsonbody_net = [
    {
        "measurement": "docker_container_net",
        "tags": {
            "host": "master",
            "TERMINUS_KEY": ""
        },
        "fields": {
            "container_id": "container_id_test",
            "rx_bytes": 197636066,
            "rx_dropped": 0,
            "rx_errors": 0,
            "rx_packets": 1348419,
            "tx_bytes": 0,
            "tx_dropped": 0,
            "tx_errors": 0,
            "tx_packets": 1021808
        }
    }
]

jsonbody_cpu = [
    {
        "measurement": "docker_container_cpu",
        "tags": {
            "host": "master",
            "TERMINUS_KEY": ""
        },
        "fields": {
            "container_id": "docker_container_cpu_test_id",
            "usage_in_kernelmode": 25010000000,
            "usage_in_usermode": 73170000000,
            "usage_percent": 4.5580631578947366
        }
    }
]

client = InfluxDBClient(host="127.0.0.1", port=8086, database='telegraf')


# client = InfluxDBClient(host="dcos-influxdb.terminus.io", port=80, database='metrics2')

def worker(interval):
    while True:
        client.write_points(jsonbody_cpu)
        time.sleep(interval)


if __name__ == "__main__":
    p = multiprocessing.Process(target=worker, args=(3,))
    p.start()
    print("p.id:", p.pid)
    print("p.name:", p.name)
    print("p.is_alive", p.is_alive())
