# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui import api as traitsui

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk

from tvtk.tvtk_classes.graph_algorithm import GraphAlgorithm


class EdgeLayout(GraphAlgorithm):
    """
    EdgeLayout - layout graph edges
    
    Superclass: GraphAlgorithm
    
    This class is a shell for many edge layout strategies which may be
    set using the set_layout_strategy() function.  The layout strategies do
    the actual work.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkEdgeLayout, obj, update, **traits)
    
    def _get_layout_strategy(self):
        return wrap_vtk(self._vtk_obj.GetLayoutStrategy())
    def _set_layout_strategy(self, arg):
        old_val = self._get_layout_strategy()
        self._wrap_call(self._vtk_obj.SetLayoutStrategy,
                        deref_vtk(arg))
        self.trait_property_changed('layout_strategy', old_val, arg)
    layout_strategy = traits.Property(_get_layout_strategy, _set_layout_strategy, help=\
        """
        The layout strategy to use during graph layout.
        """
    )

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(EdgeLayout, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit EdgeLayout properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit EdgeLayout properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit EdgeLayout properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

