import pytest
from priority_queue import PriorityQueue
from heap_priority_queue import PriorityQueue as HeapPriorityQueue

PHOTOSHOP_COMMAND = "Photoshop.exe file.psd"
HARMONY_COMMAND = "HarmonyPremium.exe -r file.xstage"
MAYA_COMMAND = "Maya.exe -noAutoloadPlugins -file file.ma"
NUKE_COMMAND = "Nuke14.0.exe -F 1-100 -x file.nk"

@pytest.mark.parametrize("queue", [PriorityQueue(), HeapPriorityQueue()])
def test_different_priorities(queue):
    queue.push({"priority": 10, "command": PHOTOSHOP_COMMAND})
    queue.push({"priority": 7, "command": PHOTOSHOP_COMMAND})
    queue.push({"priority": 1, "command": PHOTOSHOP_COMMAND})

    first_element = queue.pop()
    assert first_element["priority"] == 1
    assert first_element["command"] == PHOTOSHOP_COMMAND

    second_element = queue.pop()
    assert second_element["priority"] == 7
    assert first_element["command"] == PHOTOSHOP_COMMAND

    queue.push({"priority": 0, "command": PHOTOSHOP_COMMAND})
    third_element = queue.pop()
    assert third_element["priority"] == 0
    assert first_element["command"] == PHOTOSHOP_COMMAND

    fourth_element = queue.pop()
    assert fourth_element["priority"] == 10
    assert fourth_element["command"] == PHOTOSHOP_COMMAND
        
@pytest.mark.parametrize("queue", [PriorityQueue(), HeapPriorityQueue()])
def test_all_same_priority(queue):
    queue.push({"priority": 7, "command": HARMONY_COMMAND})
    queue.push({"priority": 7, "command": PHOTOSHOP_COMMAND})
    queue.push({"priority": 7, "command": MAYA_COMMAND})
    queue.push({"priority": 7, "command": NUKE_COMMAND})

    command_order = [HARMONY_COMMAND, PHOTOSHOP_COMMAND, MAYA_COMMAND, NUKE_COMMAND]
    command_index = 0
    while(not queue.isEmpty()):
        element = queue.pop()
        assert element["priority"] == 7
        assert element["command"] == command_order[command_index]
        command_index += 1

@pytest.mark.parametrize("queue", [PriorityQueue(), HeapPriorityQueue()])
def test_out_of_bounds_lower_priority(queue):
    with pytest.raises(ValueError):
        queue.push({"priority": -1, "command": NUKE_COMMAND})

@pytest.mark.parametrize("queue", [PriorityQueue(), HeapPriorityQueue()])
def test_out_of_bounds_upper_priority(queue):
    with pytest.raises(ValueError):
        queue.push({"priority": 12, "command": MAYA_COMMAND})

@pytest.mark.parametrize("queue", [PriorityQueue(), HeapPriorityQueue()])
def test_empty_queue(queue):
    element = queue.pop()
    assert element is None

@pytest.mark.parametrize("queue", [PriorityQueue(), HeapPriorityQueue()])
def test_missing_priority(queue):
    with pytest.raises(KeyError):
        queue.push({"command": PHOTOSHOP_COMMAND})

@pytest.mark.parametrize("queue", [PriorityQueue(), HeapPriorityQueue()])
def test_missing_command(queue):
    with pytest.raises(KeyError):
        queue.push({"priority": 3})
