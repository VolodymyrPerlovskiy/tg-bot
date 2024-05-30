from datetime import datetime, timezone 
import threading, time, subprocess, platform
import redis

Host = ""
next_call = time.time()
rs = redis.StrictRedis(host="127.0.0.1", port="6379", password="", db=0)

def ping_ok(sHost) -> bool:
    try:
        subprocess.check_output(
            "ping -{} 3 {}".format("n" if platform.system().lower() == "windows" else "c", sHost), shell=True
        )
    except Exception:
        return False

    return True

def current_status():
    aware_local_now = datetime.now(timezone.utc).astimezone().strftime("%m/%d/%Y-%H:%M:%S")
    current_state = ping_ok(Host)
    return aware_local_now, current_state

# Write health check result to redis constantly
def write_2_cache():
    global next_call
    aware_local_now = datetime.now(timezone.utc).astimezone().strftime("%m/%d/%Y-%H:%M:%S")
    current_state = ping_ok(Host) 
    next_call = next_call+3600
    rs.set(str(aware_local_now), str(current_state), ex=604800)
    threading.Timer( next_call - time.time(), write_2_cache).start()



