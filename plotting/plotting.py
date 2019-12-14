# plotting.py

# Author : aarontillekeratne
# Date : 8/12/19

# This file is part of PolicyIteration.

# PolicyIteration is free software:
# you can redistribute it and/or modify it under the terms of the GNU General
# Public License as published by the Free Software Foundation, either version 3
# of the License, or (at your option) any later version.

# PolicyIteration is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with PolicyIteration.  
# If not, see <https://www.gnu.org/licenses/>.

import numpy as np
import plotly.figure_factory as ff
from enum import Enum


class ColorScale(Enum):
    Viridis = 'viridis'
    Cividis = 'cividis'


def plot_matrix(matrix: np.ndarray, colorscale=ColorScale.Viridis):
    """
    Plots a matrix into a heat map.
    :param colorscale:
    :param matrix:
    :return:
    """

    fig = ff.create_annotated_heatmap(matrix, colorscale=colorscale.value,
                                      xgap=1, ygap=1)
    fig['layout']['yaxis']['autorange'] = "reversed"
    return fig
