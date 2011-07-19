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

from tvtk.tvtk_classes.hierarchical_box_data_set_algorithm import HierarchicalBoxDataSetAlgorithm


class ExtractDataSets(HierarchicalBoxDataSetAlgorithm):
    """
    ExtractDataSets - extracts a number of datasets.
    
    Superclass: HierarchicalBoxDataSetAlgorithm
    
    ExtractDataSets accepts a HierarchicalBoxDataSet as input and
    extracts different datasets from different levels. The output is
    HierarchicalBoxDataSet with same structure as the input with only
    the selected datasets passed through.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractDataSets, obj, update, **traits)
    
    def add_data_set(self, *args):
        """
        V.add_data_set(int, int)
        C++: void AddDataSet(unsigned int level, unsigned int idx)
        Add a dataset to be extracted.
        """
        ret = self._wrap_call(self._vtk_obj.AddDataSet, *args)
        return ret

    def clear_data_set_list(self):
        """
        V.clear_data_set_list()
        C++: void ClearDataSetList()
        Remove all entries from the list of datasets to be extracted.
        """
        ret = self._vtk_obj.ClearDataSetList()
        return ret
        

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
            return super(ExtractDataSets, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractDataSets properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ExtractDataSets properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractDataSets properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

