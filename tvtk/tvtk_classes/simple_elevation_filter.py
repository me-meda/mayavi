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

from tvtk.tvtk_classes.data_set_algorithm import DataSetAlgorithm


class SimpleElevationFilter(DataSetAlgorithm):
    """
    SimpleElevationFilter - generate scalars along a specified
    direction
    
    Superclass: DataSetAlgorithm
    
    SimpleElevationFilter is a filter to generate scalar values from a
    dataset.  The scalar values are generated by dotting a user-specified
    vector against a vector defined from the input dataset points to the
    origin.
    
    See Also:
    
    ElevationFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSimpleElevationFilter, obj, update, **traits)
    
    vector = traits.Array(shape=(3,), value=(0.0, 0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _vector_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVector,
                        self.vector)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('vector', 'GetVector'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('abort_execute', 'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text', 'vector'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SimpleElevationFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SimpleElevationFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['vector']),
            title='Edit SimpleElevationFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SimpleElevationFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

