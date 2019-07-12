# Copyright 2019 Xiaomi, Inc.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from enum import Enum

MaxChunkSize = 500
DefaultChunkSize = 20
DefaultBatch = 1

NNet2 = 2
NNet3 = 3

Nnet2Header = "<Nnet>"
Nnet2End = "</Nnet>"

TransModelHeader = '<TransitionModel>'
TransModelEnd = '</TransitionModel>'

Nnet3Header = "<Nnet3>"
Nnet3End = "</Nnet3>"

INPUT_NAME = "input"
IVECTOR_NAME = "ivector"

KaldiOps = [
    'AdditiveNoise',
    'Gemm',
    'Append',
    'BatchNorm',
    'Bias',
    'ClipGradient',
    'Identity',  # for next chunk's computaion, need to cache the node's output
    'Constant',
    'ConstantFunction',
    'Conv1d',
    'Conv',
    'Dct',
    'Distribute',
    'Dropout',
    'DropoutMask',
    'EltwiseProduct',
    'ExtractPooling',
    'FixedScale',
    'DynamicLSTM',
    'IfDefined',
    'Linear',
    'LogSoftmax',
    'LstmNonlinear',
    'Maxout',
    'Maxpooling',
    'Nonlinear',
    'NoOp',
    'TargetRMSNorm',
    'Offset',
    'PerEltOffset',
    'PerEltScale',
    'Permute',
    'PNorm',
    'Power',
    'Random',
    'Relu',
    'ReplaceIndex',
    'RestrictedAttention',
    'Round',
    'Scale',
    'ScaleOffset',
    'Scales',
    'Sigmoid',
    'SoftHinge',
    'Softmax',
    'Splice',
    'SpliceMax',
    'StatisticsExtraction',
    'StatisticsPooling',
    'Subsample',  # add subsample node to support chain models
    'Sum',
    'SumBlock',
    'SumGroup',
    'Tanh',
    'Tdnn',
    'TimeHeightConv',
    # 'Input',
    # 'Output',
    'DimRange',
]
KaldiOpType = Enum('KaldiOpType',
                   [(op, op) for op in KaldiOps],
                   type=str)

KaldiOpRawType = {
    "AdditiveNoiseComponent": 'AdditiveNoise',
    "AffineComponent": 'Gemm',
    "AffineComponentPreconditioned": 'Gemm',
    "AffineComponentPreconditionedOnline": 'Gemm',
    "BackpropTruncationComponent": 'Scale',
    "BatchNormComponent": 'BatchNorm',
    "BlockAffineComponent": 'Gemm',
    "BlockAffineComponentPreconditioned": 'Gemm',
    "ClipGradientComponent": 'ClipGradient',
    "ConstantComponent": 'Constant',
    'ConstantFunctionComponent': 'ConstantFunction',
    "Convolutional1dComponent": 'Conv1d',
    "ConvolutionComponent": 'Conv',
    "DctComponent": 'Dct',
    "DistributeComponent": 'Distribute',
    "DropoutComponent": 'Dropout',
    "DropoutMaskComponent": 'DropoutMask',
    "ElementwiseProductComponent": 'EltwiseProduct',
    "FixedAffineComponent": 'Gemm',
    "FixedBiasComponent": 'Bias',
    "FixedLinearComponent": 'Linear',
    "FixedScaleComponent": 'Scales',
    "GeneralDropoutComponent": 'Dropout',
    "LinearComponent": 'Linear',
    "LogSoftmaxComponent": 'LogSoftmax',
    "LstmNonlinearityComponent": 'LstmNonlinear',
    "MaxoutComponent": 'Maxout',
    "MaxpoolingComponent": 'Maxpooling',
    "NaturalGradientAffineComponent": 'Gemm',
    "NaturalGradientPerElementScaleComponent": 'PerEltScale',
    "NaturalGradientRepeatedAffineComponent": 'Gemm',
    "NonlinearComponent": 'Nonlinear',
    "NoOpComponent": "NoOp",
    "NormalizeComponent": 'TargetRMSNorm',
    "PerElementOffsetComponent": 'PerEltOffset',
    "PerElementScaleComponent": 'PerEltScale',
    "PermuteComponent": 'Permute',
    "PnormComponent": 'PNorm',
    "PowerComponent": 'Power',
    "RandomComponent": "Random",
    "RectifiedLinearComponent": 'Relu',
    "RepeatedAffineComponent": 'Gemm',
    "RestrictedAttentionComponent": 'RestrictedAttention',
    "ScaleComponent": 'Scale',
    "ScaleAndOffsetComponent": 'ScaleOffset',
    "SigmoidComponent": 'Sigmoid',
    "SoftHingeComponent": 'SoftHinge',
    "SoftmaxComponent": 'Softmax',
    "SpliceComponent": 'Splice',
    "SpliceMaxComponent": 'SpliceMax',
    "StatisticsExtractionComponent": 'StatisticsExtraction',
    "StatisticsPoolingComponent": 'StatisticsPooling',
    "SumBlockComponent": 'SumBlock',
    "SumGroupComponent": 'SumGroup',
    "TanhComponent": 'Tanh',
    "TdnnComponent": 'Tdnn',
    "TimeHeightConvolutionComponent": 'TimeHeightConv',
    "output-node": 'Output',
    "input-node": 'Input',
    "dim-range-node": 'DimRange',
}


NNet2Components = [
    'AdditiveNoiseComponent',
    'AffineComponent',
    'AffineComponentPreconditioned',
    'AffineComponentPreconditionedOnline',
    'BlockAffineComponent',
    'BlockAffineComponentPreconditioned',
    'Convolutional1dComponent',
    'DctComponent',
    'DropoutComponent',
    'FixedAffineComponent',
    'FixedBiasComponent',
    'FixedLinearComponent',
    'FixedScaleComponent',
    'LogSoftmaxComponent',
    'MaxoutComponent',
    'MaxpoolingComponent',
    'NonlinearComponent',
    'NormalizeComponent',
    'PermuteComponent',
    'PnormComponent',
    'PowerComponent',
    'RandomComponent',
    'RectifiedLinearComponent',
    'ScaleComponent',
    'SigmoidComponent',
    'SoftHingeComponent',
    'SoftmaxComponent',
    'SpliceComponent',
    'SpliceMaxComponent',
    'SumGroupComponent',
    'TanhComponent',
]
NNet2Component = Enum('NNet2Component',
                      [(op, op) for op in NNet2Components],
                      type=str)


NNet3Descriptors = [
    'Append',
    'Const',
    'Scale',
    'Offset',
    'Sum',
    'IfDefined',
    'ReplaceIndex',
    'Round',
    'Switch',
    'Failover',
]
NNet3Descriptor = Enum('NNet3Descriptors',
                       [(op, op) for op in NNet3Descriptors],
                       type=str)


NNet3Components = [
    'AffineComponent',
    'BackpropTruncationComponent',
    'BatchNormComponent',
    'BlockAffineComponent',
    'BlockAffineComponentPreconditioned',
    'ClipGradientComponent',
    'ConstantComponent',
    'ConstantFunctionComponent',
    'ConvolutionComponent',
    'DistributeComponent',
    'DropoutComponent',
    'DropoutMaskComponent',
    'ElementwiseProductComponent',
    'FixedAffineComponent',
    'FixedBiasComponent',
    'FixedScaleComponent',
    'GeneralDropoutComponent',
    'LinearComponent',
    'LogSoftmaxComponent',
    'LstmNonlinearityComponent',
    'MaxpoolingComponent',
    'NaturalGradientAffineComponent',
    'NaturalGradientPerElementScaleComponent',
    'NaturalGradientRepeatedAffineComponent',
    'NonlinearComponent',
    'NoOpComponent',
    'NormalizeComponent',
    'PerElementOffsetComponent',
    'PerElementScaleComponent',
    'PermuteComponent',
    'PnormComponent',
    'RandomComponent',
    'RectifiedLinearComponent',
    'RepeatedAffineComponent',
    'RestrictedAttentionComponent',
    'ScaleAndOffsetComponent',
    'SigmoidComponent',
    'SoftmaxComponent',
    'StatisticsExtractionComponent',
    'StatisticsPoolingComponent',
    'SumBlockComponent',
    'SumGroupComponent',
    'TanhComponent',
    'TdnnComponent',
    'TimeHeightConvolutionComponent',
]
NNet3Component = Enum('NNet3Component',
                      [(op, op) for op in NNet3Components],
                      type=str)


ATTRIBUTE_NAMES = {
    KaldiOpType.AdditiveNoise.name: ['std_dev'],
    KaldiOpType.Gemm.name: ['num_repeats', 'num_blocks'],
    KaldiOpType.BatchNorm.name: ['dim',
                                 'block_dim',
                                 'epsilon',
                                 'target_rms',
                                 'count',
                                 'test_mode'],
    KaldiOpType.ClipGradient.name: ['dim'],
    KaldiOpType.Conv.name: ['input_x_dim',
                            'input_y_dim',
                            'input_z_dim',
                            'filt_x_dim',
                            'filt_y_dim',
                            'filt_z_dim',
                            'filt_x_step',
                            'filt_y_step',
                            'input_vectorization'],
    KaldiOpType.Conv1d.name: ['patch_dim',
                              'patch_step',
                              'patch_stride'],
    KaldiOpType.Dct.name: ['dct_dim',
                           'reorder',
                           'keep_dct_dim'],
    KaldiOpType.Distribute.name: ['input_dim', 'output_dim'],
    KaldiOpType.Dropout.name: ['dim'],
    KaldiOpType.ReplaceIndex.name: ['var_name',
                                    'value',
                                    'chunk_size',
                                    'left_context',
                                    'right_context'],
    KaldiOpType.DimRange.name: ['dim', 'offset'],
    KaldiOpType.IfDefined.name: ['offset'],
    KaldiOpType.Linear.name: ['rank_inout',
                              'updated_period',
                              'num_samples_history',
                              'alpha'],
    KaldiOpType.LstmNonlinear.name: ['dim',
                                     'input_dim',
                                     'output_dim',
                                     'count'],
    KaldiOpType.Maxpooling.name: ['input_x_dim',
                                  'input_y_dim',
                                  'input_z_dim',
                                  'pool_x_size',
                                  'pool_y_size',
                                  'pool_z_size',
                                  'pool_x_step',
                                  'pool_y_step',
                                  'pool_z_step',
                                  'pool_size',
                                  'pool_stride'],
    KaldiOpType.TargetRMSNorm.name: ['dim',
                                     'input_dim',
                                     'block_dim',
                                     'output_dim',
                                     'target_rms',
                                     'add_log_stddev'],
    KaldiOpType.Nonlinear.name: ['count', 'block_dim'],
    KaldiOpType.Offset.name: ['offset'],
    KaldiOpType.PNorm.name: ['input_dim', 'p', 'output_dim'],
    KaldiOpType.Power.name: ['input_dim', 'power', 'output_dim'],
    KaldiOpType.Round.name: ['modulus'],
    KaldiOpType.Scale.name: ['scale', 'dim'],
    KaldiOpType.Softmax.name: ['dim'],
    KaldiOpType.Splice.name: ['dim',
                              'left_context',
                              'right_context',
                              'context',
                              'input_dim',
                              'output_dim',
                              'const_component_dim'],
    KaldiOpType.StatisticsExtraction.name: ['input_dim',
                                            'input_period',
                                            'output_period',
                                            'include_variance'],
    KaldiOpType.StatisticsPooling.name: ['input_dim',
                                         'input_period',
                                         'output_period',
                                         'left_context',
                                         'right_context',
                                         'num_log_count_features',
                                         'output_stddevs',
                                         'variance_floor', ],
    KaldiOpType.SumGroup.name: ['output_dim'],

}

CONSTS_NAMES = {
    KaldiOpType.Gemm.name: ['params', 'bias'],
    KaldiOpType.Bias.name: ['bias'],
    KaldiOpType.BatchNorm.name: ['stats_mean', 'stats_var'],
    KaldiOpType.Constant.name: ['constants'],
    KaldiOpType.ConstantFunction.name: ['constants'],
    KaldiOpType.Conv1d.name: ['params', 'bias'],
    KaldiOpType.Conv.name: ['params', 'bias'],
    KaldiOpType.Linear.name: ['params'],
    KaldiOpType.LstmNonlinear.name: ['params',
                                     'value_avg',
                                     'deriv_avg'],
    KaldiOpType.Nonlinear.name: ['value_avg',
                                 'deriv_avg',
                                 'value_sum',
                                 'deriv_sum'],
    KaldiOpType.PerEltOffset.name: ['offsets'],
    KaldiOpType.PerEltScale.name: ['params'],
    KaldiOpType.Permute.name: ['column_map', 'reorder'],
    KaldiOpType.RestrictedAttention.name: ['entropy_stats',
                                           'posterior_stats'],
    KaldiOpType.FixedScale.name: ['scales'],
    KaldiOpType.ScaleOffset.name: ['scales', 'offsets'],
    KaldiOpType.SumGroup.name: ['sizes'],
    KaldiOpType.Tdnn.name: ['time_offsets', 'params', 'bias'],
    KaldiOpType.TimeHeightConv.name: ['params', 'bias']
}
