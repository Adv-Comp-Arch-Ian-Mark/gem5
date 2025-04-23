from m5.objects import *
from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.classic.no_cache import NoCache
from gem5.components.memory.single_channel import SingleChannelDDR3_1600
from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.isas import ISA
from gem5.resources.resource import CustomResource
from gem5.simulate.simulator import Simulator
from gem5.utils.requires import requires


cache_hierarchy = NoCache()
#cache_hierarchy = MI_EXAMPLE()
memory = SingleChannelDDR3_1600()

processor = SimpleProcessor(cpu_type=CPUTypes.TIMING, num_cores=1, isa=ISA.RISCV)

# branch_pred = MyPredictor(
#     # localPredictorSize= 4096 ,
#     # localCtrBits=4,
#     # globalPredictorSize=4096,
#     # globalCtrBits=2,
#     # choicePredictorSize=2048,
#     # choiceCtrBits=2,
# )

# for core in processor.get_cores():
#     core.core.branchPred = branch_pred
#     core.core.numThreads = 1


board = SimpleBoard(
    clk_freq="3GHz",
    processor=processor,
    memory=memory,
    cache_hierarchy=cache_hierarchy,
)

board.set_se_binary_workload(
    CustomResource("/home/user/gem5/Neuromorphic_Benchmark.o")
)
#board.set_se_binary_workload(
#    CustomResource("/home/user/gem5/Regular_Benchmark.o")
#)


simulator = Simulator(board=board)
simulator.run()


#borrowed from examples on gem5 tutorials website:
print(
    "Exiting @ tick {} because {}.".format(
        simulator.get_current_tick(), simulator.get_last_exit_event_cause()
    )
)
